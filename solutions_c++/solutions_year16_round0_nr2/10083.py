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
    int t,i,in=1;
    si(t);
    while(in<=t)
    {   
     char a[1000];
     scanf("%s",a);
     int l=strlen(a),ans=0;
     if(a[0]=='-')
     ans++;
     l--;
     for(i=0;i<l;i++)
     {
        if(a[i]=='+'&&a[i+1]=='-')    
        ans+=2;
     }
     cout<<"Case #"<<in<<": "<<ans<<endl;
    in++;
    }
    return 0;
}
