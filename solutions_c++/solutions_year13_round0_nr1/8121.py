
#include<iostream>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;
char status = 'N';
char arr[16];

void check(int i, int j,int offset)
{
    char now = arr[i*4+j];


    if(now == 'T')
    {
        now = arr[i*4+j + offset];

    }
    if(now == '.')
        return;
    for ( int k  = 0 ; k< 4; k++)
    {
        if(arr[i*4+j + k*offset] != now && arr [i*4+j + k*offset] != 'T')
            break;
        if(k == 3)
        {
            status = now;
        }
    }
}

bool checkWin()
{
    if(status != 'N')
    {
       // cout<<status<<endl;
        return true;
    }

    return false;

}

void handleOneInput()
{
    status = 'N';
    bool dotExist = false;
    for(int i = 0 ;  i< 4 ; i++)
    {
        string buffer;
        getline(cin,buffer);
//cout<<"got line"<<buffer<<endl;

        for(int j = 0 ; j < 4; j++)
        {
            if(buffer[i]  == '.')
                dotExist = true;

            arr[i*4+j] = buffer[j];

        }
    }
    string null;
    getline(cin,null);

    check(0,0,5);
    if(checkWin()) return;
    check(0,3,3);
    if(checkWin()) return;
    check(0,0,4);
    if(checkWin()) return;
    check(0,1,4);
    if(checkWin()) return;
    check(0,2,4);
    if(checkWin()) return;
    check(0,3,4);
    if(checkWin()) return;
    check(0,0,1);
    if(checkWin()) return;
    check(1,0,1);
    if(checkWin()) return;
    check(2,0,1);
    if(checkWin()) return;
    check(3,0,1);
    if(checkWin()) return;

    if(dotExist)
        status = 'N';
        //cout<<"ongoing"<<endl;
    else
    status = 'D';
        //cout<<"draw"<<endl;

}





int main()
{
        char filename[]="result.txt";
    fstream fp;
    fp.open(filename, ios::out);
    if(!fp){
        cout<<"Fail to open file: "<<filename<<endl;
    }
    cout<<"File Descriptor: "<<fp<<endl;



    int c;
    freopen("A-small-attempt1.in","r",stdin);

    scanf("%d\n",&c);
    for(int i = 0; i< c ; i++)
{

        handleOneInput();
        string ps;
        if(status == 'N')
         ps = "Game has not completed";
         else if(status == 'D')
            ps = "Draw";
         else if(status == 'X')
            ps = "X won";
         else if(status == 'O')
            ps = "O won";






        fp<<"Case #"<<i+1<< ": "<<ps<<endl;

    }

     fp.close();//Ãö³¬ÀÉ®×

    return 0;
}
