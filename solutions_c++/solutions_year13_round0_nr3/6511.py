#include<iostream>
#include<string>
#include<stdio.h>
#include<fstream>
#include <sstream>
#include <cmath>
using namespace std;

string int2str(const int i)
{
    string s;
    stringstream ss(s);
    ss<<i;
    return ss.str();
}


bool isPali(const int i)
{
    string s = int2str(i);
    bool ispa = true;
    for(int i = 0; i<s.length()/2; i++)
    {
        if(s[i] != s[s.length()-1-i])
            ispa = false;
    }
    return ispa;
}

int handleOneInput()
{
    int counter = 0;

    int in1,in2;
    float sn,en;
    scanf("%d %d\n",&in1,&in2);

    sn = ceil(sqrt((float)in1));
    en = floor(sqrt((float)in2));
    //cout<<"snen:"<<sn<<" "<<en<<endl;
    for( int i = (int)sn ; i<=en; i++)
    {
        if(isPali(i))
        {
            if(isPali(i*i))
            {
                counter++;
                // cout<<"i:"<<i<<" ";
            }

        }


    }
//cout<<endl;
    return counter;
    // scanf("%d",&in1);
    // cout<<isPali(in1)<<endl;

}


int main()
{
    char filename[]="result.txt";
    fstream fp;
    fp.open(filename, ios::out);
    if(!fp)
    {
        cout<<"Fail to open file: "<<filename<<endl;
    }
    cout<<"File Descriptor: "<<fp<<endl;



    int c;
    freopen("C-small-attempt0.in","r",stdin);

    scanf("%d\n",&c);
    //cout<<c<<endl;
    for(int i = 0; i< c ; i++)
    {

        fp<<"Case #"<<i+1<<": "<<handleOneInput()<<endl;








        //  fp<<"Case #"<<i+1<< ": "<<ps<<endl;

    }

    fp.close();//Ãö³¬ÀÉ®×

    return 0;
}
