#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

bool dig[11];

bool ok(){
	FOR(i,10)
		if(!dig[i])return 0;
	return 1;
}

void add(ll n){
	while(n>0){
		dig[n%10]=1;
		n/=10;
	}
}

void solve(int prim){
	ll n;
	scanf("%lld",&n);
	if(n==0){
		printf("Case #%d: INSOMNIA\n",prim);
		return;
	}
	memset(dig,0,sizeof(dig));
	ll st=1;
	while(!ok()){
		add(n*st);
		st++;
	}
	printf("Case #%d: %lld\n",prim,n*(st-1));
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
