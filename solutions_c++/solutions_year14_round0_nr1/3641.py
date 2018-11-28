#include<iostream>
#include<fstream>
using namespace std;
int ans = 0;
int magic()
{

    int m[4][4]={0};
    int row1,i,j,row2,status=0;
    int test_case;
    cin>>row1;
    for(i=0; i<4; i++)
        for(j=0; j<4; j++)
    {
        cin>>m[i][j];
    }
    int a,b,c,d;
    a = m[row1-1][0];
    b = m[row1-1][1];
    c = m[row1-1][2];
    d = m[row1-1][3];
    cin>>row2;
    for(i=0; i<4; i++)
        for(j=0; j<4; j++)
    {
        cin>>m[i][j];
    }
    for(i=0; i<4; i++)
    {

        if(a==m[row2-1][i])
        {ans = a;status++;}
        if(b==m[row2-1][i])
        {ans = b;status++;}
        if(c==m[row2-1][i])
        {ans = c;status++;}
        if(d==m[row2-1][i])
        {ans = d;status++;}
        //cout<<"status = "<<status<<endl;

    }

    return status;


}


int main()
{
   ofstream outputfile("output.txt");
   int i=0,test=0,status;
   cin>>test;
   while(i<test)
   {
    ans = 0;
    status = magic();
    if(status == 1)
            outputfile<<"Case #"<<i+1<<": "<<ans<<endl;
    if(status >1)
        outputfile<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    if(status==0)
        outputfile<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
        i++;
   }

}
