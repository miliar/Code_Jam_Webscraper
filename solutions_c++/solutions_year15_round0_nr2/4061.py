#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>

#include <queue>
#include <utility>
#include <set>
#include <stack>
#include <vector>
#include <map>

#define YOU using
#define DONT namespace
#define SAY std

YOU DONT SAY;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
typedef pair<int,ll> pil;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef vector<pll> vll;
typedef pair<int,double> pif;
typedef pair<double,double> pff;

#define OO (int)1e9
#define MOD 1000000007
#define INF (ll)1e17

//#define max(a,b) ((a) > (b) ? (a) : (b))
//#define min(a,b) ((a) < (b) ? (a) : (b))
#define exl(i,l,r) ((i) > (l) && (i) < (r))
#define inl(i,l,r) ((i) >= (l) && (i) <= (r))

#define repp(i,a,b,d) for(int i=a;i<=b;i+=d)
#define rep(i,a,b) repp(i,a,b,1)
#define revv(i,a,b,d) for(int i=a;i>=b;i-=d)
#define rev(i,a,b) revv(i,a,b,1)

#define mp make_pair
#define pb push_back

#define ff first
#define ss second

int tc;
int n;
int arr[1005];
int memo[1005][1005];

int rec(int idx,int mx){
	if(idx>n)return mx;
	if(memo[idx][mx]!=-1)return memo[idx][mx];
	
	int ans = OO;
	rep(i,1,arr[idx]){
		ans = min(ans, i-1 + rec(idx+1,max(mx,arr[idx]/i + ((arr[idx]%i==0)?0:1))));
	}
	return memo[idx][mx] = ans;
}

int main(){
	scanf("%d",&tc);
	rep(z,1,tc){
		scanf("%d",&n);
		
		rep(i,1,n){
			scanf("%d",&arr[i]);
		}
		
		memset(memo,-1,sizeof(memo));
		
		printf("Case #%d: %d\n",z,rec(1,0));
	}
	return 0;
}

