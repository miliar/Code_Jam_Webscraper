#include<bits/stdc++.h>
using namespace std;

int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
    long long tc=0,t,i,c,m,f;
    string s;
    scanf("%lld",&t);
    while(t--)
    {
        f=0;
        c=0;
        cin>>s;
        if(s[0]=='+') {f=1;c=0;}
        else if(s[0]=='-') {c=1;}
        for(i=1;s[i]!='\0';i++)
        {
            if(s[i]=='+') f=1;
            else if(s[i]=='-')
            {
                if(f==1) {f=0;c+=2;}
            }
        }
        printf("Case #%lld: %lld\n",++tc,c);
        s="";
    }
}
