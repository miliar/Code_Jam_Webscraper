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
char a[110];
int b[110],c[110];
int main()
{
    ip;
    op;
	int i,j,k,T,K,l,ans;
	cin>>T;
	getchar();
	for(K=1;K<=T;K++)
	{
	    CLR(a); CLR(b); CLR(c);
	    scanf("%s",&a);
	    l=strlen(a);
	    for(i=0;i<l;i++)
        {
            if(a[i]=='+') b[i+1]=1;
            else b[i+1]=0;
        }
        ans=0;
        if(b[1]==1) c[1]=0;
        else c[1]=1;
        //cout<<"1 "<<c[1]<<endl;
        for(i=2;i<=l;i++)
        {
            if(b[i]==1) c[i]=c[i-1];
            else if(b[i]==0&&b[i-1]==0) c[i]=c[i-1];
            else c[i]=c[i-1]+2;
            //cout<<i<<" "<<c[i]<<endl;
        }
		printf("Case #%d: %d\n",K,c[l]);
	}
	return 0;
}
