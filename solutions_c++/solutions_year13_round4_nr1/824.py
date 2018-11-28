#include<iostream>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

ll gcd(ll r0, ll r1)
{
    if(r0==0 || r1==0)
    return 1;

    if(r0<r1)
    return gcd(r1,r0);

    if(r0%r1==0)
    return r1;

    return gcd(r1,r0%r1);
}
ll findInverse(ll a, ll b)
{
    ll x[3];
    ll y[3];
    ll quotient  = a / b;
    ll remainder = a % b;
    x[0] = 0;
    y[0] = 1;
    x[1] = 1;
    y[1] = quotient * -1;

    ll i = 2;
    for (; (b % (a%b)) != 0; i++)
    {
        a = b;
        b = remainder;
        quotient = a / b;
        remainder = a % b;
        x[i % 3] = (quotient * -1 * x[(i - 1) % 3]) + x[(i - 2) % 3];
        y[i % 3] = (quotient * -1 * y[(i - 1) % 3]) + y[(i - 2) % 3];
    }
    //x[i — 1 % 3] is inverse of a
    //y[i — 1 % 3] is inverse of b
    return x[(i - 1) % 3];
}

struct data {
  int x,y,p;
};
ll mod = 1000002013;
int t,n,m;

bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
data a[1000];
ll b[2000], p[2000][2000];
int tc;

int see(int at) {
  REP(i,tc) {
    if(at==b[i]) {
      return i;
    }
  }
  return -1;
}

ll get(int s, int e, ll p) {
  ll dis = e-s;
  dis = n*dis - (dis*(dis-1))/2;
  dis%=mod;
  dis*=p;
  dis%=mod;
  return dis;
}

int main()
{
   //freopen("input.txt","r",stdin);
   //freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
     si(n);
     si(m);
     REP(i,m) {
       si(a[i].x);
       si(a[i].y);
       si(a[i].p);
     }
     ll tot = 0;
     REP(i,m) {
       ll dis = (a[i].y-a[i].x);
       dis = n*dis - (dis*(dis-1))/2;
       dis%=mod;
       dis*=a[i].p;
       dis%=mod;
       tot+=dis;
       tot%=mod;
     }
     sort(a,a+m,myfunction);
     REP(i,m) {
       b[2*i]=a[i].x;
       b[i*2+1]=a[i].y;
     }
     sort(b,b+2*m);
     int at=0;
     FOR(i,1,2*m) {
       if (b[at]!=b[i]) {
         b[at+1]=b[i];
         at++;
       }
     }
     tc = at+1;
     memset(p,0,sizeof(p));
     REP(i,m) {
       p[see(a[i].x)][see(a[i].y)]+=a[i].p;
     }
     ll totn=0;
     REP(i,tc) {
       for (int j=tc-1; j>=i ;j--) {
         ll per = p[i][j];
         REP(k,i) {
           FOR(l,i,j) {
             if (per>0 && p[k][l]>0) {
               ll maxi = min(per,p[k][l]);
               p[k][l]-=maxi;
               p[i][j]-=maxi;
               p[i][l]+=maxi;
               p[k][j]+=maxi;
               per-=maxi;
             }
             if(per==0) {
               break;
             }
           }
           if (per == 0) {
             break;
           }
         }
       }
     }
     REP(i,tc) {
       FOR(j,i,tc) {
          ll dis = (b[j]-b[i]);
          dis = n*dis - (dis*(dis-1))/2;
          dis%=mod;
          dis*=p[i][j];
          dis%=mod;
          totn+=dis;
          totn%=mod;
       }
     }
     tot-=totn;
     while(tot<0) {
       tot+=mod;
     }
     printf("Case #%d: %lld\n", prob+1, tot);
   }

   //system("pause");
   return 0;

}
