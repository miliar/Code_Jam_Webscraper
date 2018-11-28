#include<iostream>
#include<cstdio>
#include<fstream>
#include<string>
#include<cstdlib>
#include<iomanip>
#include<sstream>
using namespace std;
int *cc1,*cc2;
char *t1,*t2;
int matchExact(int sl,int ll,int i,int j,string sstr,string lstr)
{
    for(int k=i,z=j;k<ll&&z<sl;k++,z++)
    {
            if(lstr[k]!=sstr[z])
            {
                return 0;
            }
    }
    return 1;
}
int createArray(string x,int len,int index)
{
    int *cc=new int[len];
    char *t=new char[len];
    int len_new;
    for(int i=0,j=0;j<x.length();j++)
    {
        if(j==0)
        {
            t[i]=x[j];
            cc[i]=1;
            len_new=1;
        }
        else
        {
            if(x[j]==x[j-1])
            {
                cc[i]++;
            }
            else
            {
                i++;
                t[i]=x[j];
                cc[i]=1;
                len_new++;
            }
        }
    }
    if(index==1)
    {
        t1=t;
        cc1=cc;
    }
    else
    {
        t2=t;
        cc2=cc;
    }
    return len_new;
}
string matchStrings(string x,string y)
{
    int xlen=createArray(x,x.length(),1);
    int ylen=createArray(y,y.length(),2);
       cout<<endl;
    int count=0;
    if(xlen!=ylen)
        return "Fegla Won";
    for(int i=0;i<xlen;i++)
    {
        if(t1[i]==t2[i])
        {
            if(cc1[i]<cc2[i])
                count+=cc2[i]-cc1[i];
            else if(cc1[i]>cc2[i])
                count+=cc1[i]-cc2[i];
        }
        else
        {
            return "Fegla Won";
        }
    }
    stringstream ss;
    ss<<count;
    string dc=ss.str();
    return dc;
}
int main()
{
    int n;
    int t;
    fstream fin;
    string x,y;
    fin.open("A-small-attempt3.in",ios::in);
    fin>>t;
    int i=0;
    fstream fout;
    fout.open("out.txt",ios::out);
    while(i++<t)
    {
        fin>>n;
        fin>>x>>y;
        fout<<"Case #"<<i<<": "<<matchStrings(x,y)<<endl;
    }
    fout.close();
}
