#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Blo.txt","w",stdout);
    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        string s;
        cin>>s;
        int n=s.length();
        int j;
        for(j=n-1;j>=0;j--)
        {
            if(s[j]=='-')
                break;
        }
        if(j<0)
            cout<<"Case #"<<i<<": 0"<<"\n";
        else
        {
            int count=0;
            for(int k=0;k<j;k++)
            {
                if(s[k]!=s[k+1])
                    count++;
            }
            cout<<"Case #"<<i<<": "<<count+1<<"\n";
        }
    }

    return 0;
}

