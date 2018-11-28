#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
char str[200];
int main()
{
    ll t,n,i,ans,j;
    ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    ll r=1;
    while(r<=t)
    {
        cin>>str;
        n=strlen(str);
        ll count=0;
        for(i=n-1;i>=0;i--)
        {
            if(str[i]=='-')
            {
                for(j=0;j<=i;j++)
                {
                    if(str[j]=='+')
                    str[j]='-';
                    else
                    str[j]='+';
                }
                count++;
            }
        }
        cout<<"Case #"<<r<<": "<<count<<endl;
        r++;

    }
}

