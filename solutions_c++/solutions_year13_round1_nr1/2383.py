#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ITER(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define MOD 1000000007

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int ll;

int main(){
	freopen("new1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int test;
	int cases=0;
	for(scanf("%d",&test);test>0;test--){
		ll r,t;
		scanf("%lld%lld",&r,&t);
		int i;
		for(i=1;i*i<=t;i++) if(2*i*i+i*(2*r-1)>t) break;
		printf("Case #%d: %d\n",++cases,i-1);
	}
	return 0;
}
