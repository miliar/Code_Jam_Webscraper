#include<stdio.h>
#include<fstream>
#include<iostream>
using namespace std;

int main()
{ int t=0,sm=0,total=0,r=1,count1=0,n=0;
string s;

ofstream outfile;
outfile.open("C:\\Users\\jhon\\Desktop\\output.in", ios::out | ios::trunc );

ifstream infile;
infile.open("C:\\Users\\jhon\\Desktop\\A-large.in");


infile>>t;
while(t--)
{
        infile>>sm;
        infile>>s;

        count1=0;
        total=0;
    for(int i=0;i<sm+1;i++)
    {
        if((int(s[i])-48)!=0)
            n=i;
    }
    for(int i=0;i<n;i++)
    {
        count1+=(int(s[i])-48);
        if(count1<i+1)
        {
            total+=((i+1)-count1);
            count1+=((i+1)-count1);

        }
    }
    outfile<<"case #"<<r<<": "<<total<<endl;
    r++;
}
return 0;
}
