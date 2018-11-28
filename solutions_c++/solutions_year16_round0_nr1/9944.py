#include<bits/stdc++.h>
#define pb push_back
#define ull unsigned long long
#define lli long long int
#define max(a,b) ((a>b)?a:b)
#define min(a,b) ((a<b)?a:b)
#define pulli(n) printf("%llu\n",n);
#define sulli(n) scanf("%llu",&n);
#define slli(n) scanf("%lld",&n)
#define si(n) scanf("%d",&n)
#define sd(n) scanf("%lf",&n)
#define pd(n) printf("%lf\n",n)
#define pi(n) printf("%d\n",n)
#define plli(n) printf("%lld\n",n)
#define iofast (ios_base::sync_with_stdio(false))
using namespace std;
int main()
{
    iofast;
    long long t,caseno=1,i,in;
    slli(t);
    while(caseno<=t)
    {   
     slli(in);
     if(in==0)
     cout<<"Case #"<<caseno<<": "<<"INSOMNIA\n";
     else
     {
     lli count=0,temp=in;
     bool a[10]={0};
     i=1;
     while(count<10)
     {
        temp=in*i;
        while(temp!=0)
        {
            if(a[temp%10]==0)
            {
                a[temp%10]=1;
                count++;
            }
            temp/=10;
        }
        i++;
     }
     cout<<"Case #"<<caseno<<": "<<in*(i-1)<<endl;
     }
     caseno++;
    }
    return 0;
}
