#include<iostream>
#include<stdio.h>
using namespace std;
bool test=true;
int main()
{
    int t,k,ans,i,n;
    bool first,neg;
    char s[102];
    if(!test)
    {
        freopen("B-large.in","r",stdin);
        freopen("outpancakeslarge.txt","w",stdout);
    }
    cin>>t;
    for(k=1;k<=t;k++)
    {
        ans=0;
        neg=0;
        n=0;
        cin>>s;
        if(s[0]=='-')
            first=true;
        else
            first=false;
        neg=first;
        for(i=0;s[i]!='\0';i++)
        {
            if(s[i]=='+')
            {
                if(neg)
                {
                    n++;
                    neg=false;
                }
            }
            else
            {
                if(!neg)
                {
                    neg=true;
                }
            }
        }
        if(neg)
            n++;
        if(first)
            ans=1+(n-1)*2;
        else
            ans=n*2;
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
