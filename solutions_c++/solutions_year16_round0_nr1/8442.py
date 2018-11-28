/*
Author: Ashfaque Ahmed , CSE-12 , MIST.
Date:
Description :
*/
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>

#define ip freopen("in.txt","r",stdin)
#define op freopen("out.txt","w",stdout)
#define SET(a) memset(a,-1,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define pb push_back
#define mp make_pair

#define max(a,b) ((a>b)?a:b)
#define min(a,b) ((a<b)?a:b)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define MAX(a) (*max_element(all(a)))
#define MIN(a) (*min_element(all(a)))
#define LB(a,x) (lower_bound(all(a),x)-a.begin())
#define UB(a,x) (upper_bound(all(a),x)-a.begin())
#define countbit(x) __builtin_popcount(x)

#define pi acos(-1)
#define M 1000007
#define I (1<<30)
#define MD 100000007
#define eps 1e-7
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> ii;
ll GCD (ll a, ll b) {return (b==0?a:GCD(b,a%b));}
ll LCM (ll a, ll b) {return ((a*b)/GCD(a,b)); }
ll BMOD(ll a,ll b,ll m){if(b==0)return 1;ll x=BMOD(a,b/2,m);x=(x*x)%m;if(b%2==1)x=(x*a)%m;return x; }
ll POW(ll a,ll b){if(b==0)return 1;ll x=POW(a,b/2);x=(x*x);if(b%2==1)x=(x*a);return x; }
ll MINV(ll a) { return BMOD(a,MD-2,MD); }
ull next_popcount(ull a) { ull b=(a&-a); ull c=a+b; return ((((c^a)>>2)/b)|c); }

struct pt
{
	int x,y;
};
//bool cmp(pair < int , int > a, pair < int, int > b){ return a.second < b.second;}

int main()
{
    ip;
    op;
	int i,j,k,T,K,f,p,n,ans,q;
	int a[10],b[10];
	cin>>T;
	for(K=1;K<=T;K++)
	{
	    scanf("%d",&n);
	    CLR(b); ans=0;
        for(i=1;i<=100;i++)
        {
            CLR(a);
            k=n*i; f=1; q=k;
            while(k>0)
            {
                p=k%10;
                //cout<<k<<" "<<p<<endl;
                a[p]=1;
                k=k/10;
            }
            for(j=0;j<=9;j++) if(a[j]==1) b[j]=1;
            f=1;
            for(j=0;j<=9;j++) if(b[j]==0) { f=0; break; }
            if(f==1) { ans=q; break; }
        }
        if(i>100) printf("Case #%d: INSOMNIA\n",K);
		else printf("Case #%d: %d\n",K,ans);
	}
	return 0;
}
