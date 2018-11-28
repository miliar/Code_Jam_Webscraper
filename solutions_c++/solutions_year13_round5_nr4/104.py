#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<cstdlib>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;

#define mp make_pair
#define pb push_back

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

//char a[210];
int n;

double memo[1<<21];

double saiki(int x){
	if(x==0)return 0.0;
	if(memo[x] > -1) return memo[x];
	double gain = 0.0;
	rep(i, n){
		int cnt = n;
		for(int j=i; j<n; ++j){
			if(x & (1<<j)){
				gain += cnt;
				int xx = x - (1<<j);
				gain += saiki(xx);
				goto tugi;
			}else{
				--cnt;
			}
		}
		for(int j=0; j<i; ++j){
			if(x & (1<<j)){
				gain += cnt;
				int xx = x - (1<<j);
				gain += saiki(xx);
				goto tugi;
			}else{
				--cnt;
			}
		}
tugi:;
	}
	return (memo[x] = gain / n);
}

double solve(){
//	scanf("%s", a);
//	n = strlen(a);
	string s; cin >> s;
	n = s.length();
	int x=0;
	rep(i,n) if(s[i]=='.') x += (1<<i);
	rep(i,(1<<21)) memo[i] = -2.0;
	return saiki(x);
}

int main(){
	int casenum; cin >> casenum;
	rep(cas, casenum){
		printf("Case #%d: %.13f\n", cas+1, solve());
	}
	return 0;
}

