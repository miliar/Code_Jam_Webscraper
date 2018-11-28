#include<bits/stdc++.h>
using namespace std;
const double pi = atan(1.0)*4.0;
typedef long long ll;
const int INF = 1000*1000*1000;
int gcd(int a,int b){return a?gcd(b%a,a):b;}
int  _pow(int base, int exp){return exp == 0 ? 1 : base * _pow(base, exp - 1);}
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
int prime(int p)
{
    int c=0;
    for(int i=1;i<=sqrt(p);i++)
    {
        if(p%i==0 and p!=1)
            c++;
    }
    if(c==1) return 1;
    return 0;
}
int solve()
{
    int N,i;int a[10003];
    cin>>N;int sum=0;
    REP(i,N)
    {
        cin>>a[i];
    }
    for(int i=1;i<N;i++)
    {
        if(a[i-1]>a[i])
        {
            sum+=a[i-1]-a[i];
        }

    }
    cout<<sum<<" ";
    int m=0;
    for(int i=1;i<N;i++)
    {
        if((a[i-1]-a[i])>0 && (a[i-1]-a[i])>m)
        {
            m=a[i-1]-a[i];
        }
    }
    int sum1=0;
    for(int i=0;i<N-1;i++)
    {
        int mi=min(a[i],m);
        if(a[i]==mi)
            sum1+=a[i];
        else sum1+=m;
    }
    cout<<sum1;
}
int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    cin>>t;
    for(int c=1;c<=t;c++)
    {
        printf("Case #%d: ",c);
        int g=solve();

        cout<<endl;
    }
   return 0;
}




























