#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define uint unsigned int

typedef pair<int,int> pii;
#define x first
#define y second

#define read(n) scanf("%d",&n)
#define readll(n) scanf("%lld",&n)
#define read2(n,m) scanf("%d%d",&n,&m)
#define read3(n,m,l) scanf("%d%d%d",&n,&m,&l)

#define fr(i,n)     for(int i=0;i<n;i++)
#define frr(i,a,b)   for(int i=a;i<b;i++)
#define rf(i,n)     for(int i=n-1;i>=0;i--)

#define init(mem,v) memset(mem,v,sizeof(mem))

#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#define DB4(a, b, c, d)    cout<<__LINE__<<" :: "<<#a<< ": "<<a<<" | "<<#b<< ": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;

int main(){
    int t;
    read(t);
    double c,f,x;

    for(int ii=1;ii<=t;ii++){
        scanf("%lf%lf%lf",&c,&f,&x);

        double ans=x;
        double rate=2;
        double tm=0;
        for(int buys=0;buys<=1000001;buys++){
            ans=min(ans,tm+x/rate);
            tm+=c/rate;
            rate+=f;
        }
        printf("Case #%d: %.9lf\n",ii,ans);
    }
}
