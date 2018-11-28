#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
char s[101];
void flip(int j)
{
    int i;
    char t;
    t=s[0];
    for(i=0;i<=j;i++)
    {
        if(t=='-')
          s[i]='+';
        else
          s[i]='-';
    }
}
int main()
{
    int n,i,k;
    char t='0';
    long long count;
    ifstream infile("input1.txt");
    ofstream outfile("output1.txt");
    infile>>n;
    for(k=1;k<=n;k++)
    {
        infile>>s;
        count=0;
        t='0';
        for(i=0;s[i]!='\0';i++)//make the whole string similar either all '+' or all '-'
        {
            if(t=='0')
             t=s[i];
            else
            {
                if(t!=s[i])
                 {
                    flip(i-1);
                    count++;
                    t=s[i];
                 }
            }
        }
        if(s[0]=='-')
         count++;
        outfile<<"Case #"<<k<<": "<<count<<"\n";
    }
    infile.close();
    outfile.close();
    return 0;
}
