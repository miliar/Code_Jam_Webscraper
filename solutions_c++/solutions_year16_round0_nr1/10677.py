#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int sa[10]={0};
bool check()
{
    for(int i=0;i<10;i++)
        if(sa[i]==0)
            return false;
    return true;
}
void setzero()
{
    for(int i=0;i<10;i++)
        sa[i]=0;
}
void digit(int a)
{
    int b;
    while(a!=0)
    {
        b=a%10;
        a=a/10;
        sa[b]=1;
    }
}
int main()
{
    int t,w;
    ifstream fin("A.in");
    ofstream fout("A_output.txt");
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        int b,a;
        fin>>a;
        cout<<a<<endl;
        b=a;
        if(a==0)
            fout<<"Case #"<<i<<":"<<" INSOMNIA\n";
        else
        {
            while(!check())
            {
                digit(b);
                b+=a;
            }
            fout<<"Case #"<<i<<": "<<b-a<<endl;
        }
        setzero();
    }
    return 0;
}
