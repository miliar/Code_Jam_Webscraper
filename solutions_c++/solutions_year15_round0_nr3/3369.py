#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
long long int o,i=0;
int a,b;
int matrix[5][5]={{0,1,2,3,4},
                  {1,1,2,3,4},
                  {2,2,-1,4,-3},
                  {3,3,-4,-1,2},
                  {4,4,3,-2,-1}};
string inp;
int c1()
{
    a=inp[i]-103;
    for(i;i<o;i++)
    {
        if(a==1 && i==o-1)
        {
            return 1;
        }
        b=matrix[abs(a)][inp[i+1]-103];
        if(a<0)
            b=b*-1;
        a=b;
    }
    return 0;
}
int c4()
{
    a=inp[i]-103;
    for(i;i<o;i++)
    {
        if(a==4)
        {
            if(i==o-1)
                return 1;
            else
            {
                i++;
                return c1();
            }
        }
        b=matrix[abs(a)][inp[i+1]-103];
        if(a<0)
            b=b*-1;
        a=b;
    }
    return 0;
}
int c3()
{
    a=inp[i]-103;
    for(i;i<o-1;i++)
    {
        if(a==3)
        {
            i++;
            return c4();
        }
        b=matrix[abs(a)][inp[i+1]-103];
        if(a<0)
            b=b*-1;
        a=b;
    }
    return 0;
}
int c2()
{
    i=0;
    a=inp[i]-103;
    for(i;i<o-1;i++)
    {
        if(a==2)
        {
            i++;
            return c3();
        }
        b=matrix[abs(a)][inp[i+1]-103];
        if(a<0)
            b=b*-1;
        a=b;
    }
    return 0;
}
int main()
{
    ifstream in;
    ofstream out;
    out.open("out1.txt",ios::out);
    in.open("inp.txt",ios::in);
    int x;
    in>>x;
    int l=x;
    long long int n,m;
    while(x--)
    {
        in>>n>>m;
        o=n*m;
        string t="";
        char ino;
        inp="";
        for(int i=0;i<n;i++)
        {
            in>>ino;
            t+=ino;
        }
        for(int i=0;i<m;i++)
            inp+=t;
        int f=0;
        f=c2();
        out<<"Case #"<<l-x<<": ";
        if(f==1)
            out<<"YES\n";
        else
            out<<"NO\n";
    }
    in.close();
    out.close();
    return 0;
}
