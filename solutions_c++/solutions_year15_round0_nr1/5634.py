#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{   freopen("A-large.in","r",stdin);
    freopen("standbig_out.txt","w",stdout);
    int t,count=0,i,n,k=0,d,s=0;
    char str[1005];
    cin>>t;
    while(k<t)
    {   count=0;
        d=0;s=0;
        cin>>n>>str;
        for(i=0;i<=n;i++)
        {   d=str[i]-'0';
            if(i<=s)
        { s+=d;
        }
        else{
            count+=i-s;
            s+=d+(i-s);
        }

        }
        cout<<"Case #"<<k+1<<": "<<count<<endl;
        k++;
    }
}
