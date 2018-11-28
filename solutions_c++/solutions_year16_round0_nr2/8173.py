#include<cstring>
#include<iostream>
#include<cstdio>
using namespace std;

void reverseflip(string &s,int len)
{
    int l=0,r=len-1;
    char c;
    while(l<=r)
    {
        if(l==r)
        {
            s[l]=(s[r]=='+'?'-':'+');
            ++l;
            --r;
        }
        else
        {
            c=s[l];
            s[l]=(s[r]=='+'?'-':'+');
            s[r]=(c=='+'?'-':'+');
            ++l;
            --r;
        }
    }
}


int minimumflips(string s)
{
    int len=s.length()-1;
    int r=len,p,steps=0;
    while(r>=0)
    {
        if(s[r]=='+')
            --r;
        else if(s[0]=='-')
        {
            ++steps;
            reverseflip(s,r+1);
        }
        else
        {
            p=r-1;
            while(s[p]=='-')
            {
                --p;
            }
            reverseflip(s,p+1);
            reverseflip(s,r+1);
            steps+=2;
        }
    }
    return steps;
}


int main()
{
    freopen("binput2.in","r",stdin);
    freopen("cjout2.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;++i)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<i<<": "<<minimumflips(s)<<endl;
    }
    return 0;
}
