#include <cstring>
#include<complex>
#include<cstdio>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<set>
#include<list>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<climits>
#include<cstdlib>
#define snd(a) scanf("%d",&(a))
#define snlld(a) scanf("%lld",&(a))
#define rep(i,n) for((i)=0;(i)<(n);(i)+=1)
#define reps(i,s,n) for((i)=(s);(i)<(n);(i)+=1)
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define pb push_back
#define pf push_front
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define fill(a,v) memset((a),(v),sizeof(a))
#define sz size()
#define mp make_pair
#define N 100010
#define mod  1000000007
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
template<class T> inline T poww(T b,T p){ll a=1;while(p){if(p&1){a=(a*b);}p>>=1;b=(b*b);}return a;}
template<class T> inline T modpoww(T b,T p,T mmod){ll a=1;while(p){if(p&1){a=(a*b)%mmod;}p>>=1;b=(b*b)%mmod;}return a%mmod;}
template<class T>  inline T gcd(T a,T b){ if(b>a)return gcd(b,a);return ((b==0)?a:gcd(b,a%b));}
template<class T> inline void scan(vector<T>& a,int n){T b;int i; rep(i,n){cin>>b;a.pb(b);}}
#define modd  20071027
#define pii pair<int,int>
#define vpii vector<pii >
#define vi vector<int>
#define vvi vector<vi >
#define vl vector<long long>
#define fr first
#define sd second
//ios_base::sync_with_stdio(0);
#define maxn 1001000
double c,f,x;
double getTime(int n){
    double s=2,a=0;
    while(n){
        a+=c*1.0/s;
        s+=f;
        n--;
    }
    a+=x*1.0/s;
    return a;
}
int main(){
    int i,j,k,t,tt=0,l,r,lth,rth;
    double a,b,h,ans;
    snd(t);
    while(t--){
        tt++;
        cin>>c>>f>>x;
        ans=x*1.0/2;
        l=0,r=100010;
        while(l<=r){
           // cout<<"ans="<<ans<<" l="<<l<<" r="<<r<<":\n";
            lth=(2*l+r)/3;
            rth=(2*r+l)/3;
            a=getTime(lth);
            b=getTime(rth);
            if(a<b){
                ans=min(ans,a);
                r=rth-1;
            }
            else {
                l=lth+1;
                ans=min(ans,b);
            }
        }
        printf("Case #%d: %.7lf\n",tt,ans);
    }



}














