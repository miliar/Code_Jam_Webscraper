#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
bool check(char *a)
{
    for(int i=0;i<strlen(a);i++)
        if(a[i]=='-')
            return false;
    return true;
}
void invert(char *a,int i,int j)
{
    if(i==0&&j<=0)
    {
        if(a[i]=='+')
            a[i]='-';
        else
            a[i]='+';
    }
    else
    {
    for(int i=0;i<=j;i++)
    {
        if(a[i]=='+')
            a[i]='-';
        else if(a[i]=='-')
            a[i]='+';
    }
    }
}
int main()
{
    int t;
    ifstream fin("B-large.in");//change input file name
    ofstream fout("output.txt");//change output file name
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        char a[200];
        fin>>a;
        int c=0;
        while(!check(a))
        {
            int j=0,t=1;
            while(t==1)
            {
                if(a[j]=='-'&&(a[j+1]=='+'||j+1==strlen(a)))
                {
                    invert(a,0,j);
                    t=0;c++;
                    //cout<<a<<endl;
                }
                //j=(j+1)%(strlen(a)-1);
                j++;
            }
            t=0;
        }
        fout<<"Case #"<<i<<": "<<c<<endl;
    }
}
