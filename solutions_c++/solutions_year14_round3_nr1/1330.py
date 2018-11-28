#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

long long po[45];

long long gcd(long long x,long long y)
{
         if(y==0)
                 return x;
         else
             return gcd(y,x%y);
}

int main()
{
    char s[30];
    long long flag,n,test,i,t,p,q,num,den,g,res,res1;
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    po[0]=1;
    for(i=1;i<45;i++)
    {
        po[i]=po[i-1]*2;
    }
    cin >> test;
    t=1;
    while(t<=test)
    {
        flag=0;
        cin >> s;
        n=strlen(s);
        p=0;
        q=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='/')
            {
                flag=1;
                continue;
            }
            else if(flag==0)
                p=10*p+(s[i]-'0');
            else
                q=10*q+(s[i]-'0');
        }
        cout << "Case #" << t << ": ";
        g=gcd(p,q);
        p=p/g;
        q=q/g;
        den=-1;
        for(i=0;i<45;i++)
        {
            if(q==po[i])
            {
                den=i;
                break;
            }
        }
        if(den==-1)
            cout << "impossible" << endl;
        else
        {
            for(i=0;i<45;i++)
            {
                if(g==po[i])
                    break;
            }
            res1=i;
            for(i=0;i<45;i++)
            {
                if(p<po[i])
                    break;
            }
            i=i-1;
            res=den-i;
         //   res=res+res1;
            cout << res << endl;
        }
        t++;
    }
    return 0;
}
