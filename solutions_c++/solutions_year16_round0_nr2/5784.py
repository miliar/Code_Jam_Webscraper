#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int rec(string s,int e)
{
    int i,j;
    if(e==-1)
        return 0;
    if(e==0)
        return 1;
    for(i=e-1;i>=0;i--)
    {
        if(s[i]=='-')
            {
                break;
            }
    }
    if(i==-1)
        return 2;
    else
    {
        for(j=e-1;j>=0;j--)
            if(s[j]=='+')
                break;
        if(s[j]==-1)
            return 1;
        else
        {
            for(i=j;i>=0;i--)
                if(s[i]=='-')
                break;
            return 2+rec(s,i);
        }
    }
}
int main()
{
    ifstream fp;
    fp.open("B-large.in",ios::in);
    ofstream fo;
    fo.open("out3.txt",ios::out);
    int t,count;
    fp>>t;
    int i,j;
    string ch;
    char c[200];
    for(i=1;i<=t;i++)
    {
        fp>>ch;
        count=0;
        for(j=ch.length()-1;j>=0;j--)
        {
            if(ch[j]=='-')
            {
                break;
            }
        }
        if(j==-1)
        {
            count=0;
        }
        else
        {
            count=rec(ch,j);
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
        fo<<"Case #"<<i<<": "<<count<<endl;
    }
}
