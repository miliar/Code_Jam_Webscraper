#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<string.h>
#include<set>
#include<map>
using namespace std;

typedef long long Int;
#define FOR(i,a,b)  for(int i=(a);i<=(b);++i)
#define sz(s) (int)(s).size()
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
void assert(bool x){if(!x)throw -1;}
const int inf = 1000000000;
const int MOD = 1000002013;
const double pi = acos(-1.0);
const Int INF = inf*(Int)inf;

Int get1(Int n,Int p){
	Int cnt=(1LL<<n);
	Int low=1,high=cnt;
	while(low<high){
		Int mid=(low+high)/2+1;
		Int place=1;
		Int deg=1;
		while(mid-(1LL<<deg)+1>=1){
			place+=(1LL<<(n-deg));
			deg++;
		}
		if(place<=p)low=mid;else high=mid-1;
	}
	return high-1;
}

Int get2(Int n,Int p){
	Int cnt=(1LL<<n);
	Int low=1,high=cnt;
	while(low<high){
		Int mid=(low+high)/2+1;
		Int place=cnt;
		Int deg=1;
		while(mid+(1LL<<deg)-1<=cnt){
			place-=(1LL<<(n-deg));
			deg++;
		}
		if(place<=p)low=mid;else high=mid-1;
	}
	return high-1;
}

pair<Int,Int> solve(){
	Int n,p;
	cin>>n>>p;
	return mp(get1(n,p),get2(n,p));
}


int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","wb",stdout);
	int tests;
	scanf("%d\n",&tests);
	for(int test_id=1;test_id<=tests;++test_id){
		pair<Int,Int> ans = solve();
		cout<<"Case #"<<test_id<<": "<<ans.first<<" "<<ans.second<<endl;
	}
}  