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
#define _maxn 1001000
int a[4][4],b[4][4];
int main(){
    int i,j,k,t,tt=0,r1,r2,ans;
    snd(t);
    while(tt<t){
        tt++;
        snd(r1);
        r1--;
        rep(i,4)rep(j,4)snd(a[i][j]);
        snd(r2);
        r2--;
        rep(i,4)rep(j,4)snd(b[i][j]);
        int ct=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++){
                if(a[r1][i]==b[r2][j]){
                    ans=a[r1][i];
                    ct++;break;
                }
            }
        if(ct==1){
            printf("Case #%d: %d\n",tt,ans);
        }
        else if(ct>1){
            printf("Case #%d: Bad magician!\n",tt);
        }
        else{
             printf("Case #%d: Volunteer cheated!\n",tt);
        }


    }
    return 0;


}





















