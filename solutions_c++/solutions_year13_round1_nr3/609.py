#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>


using namespace std;
const int MODULO = 1000000007; // check!!!
const int INF = 100000000; //1e8

typedef long long ll;
typedef pair<int,int> Pii;
typedef pair<ll,ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())

int n,m,k;
int a[20];
int b[20];

int p[] = {2,3,5,7,11};

vector<int> solve(){
	FOR(i,k) cin>>a[i];
	FOR(i,k) b[i] = a[i];
	int p_count[20] = {};
	FOR(i,k){
		FOR(j,5){
			int cnt = 0;
			while(a[i] % p[j] == 0) a[i] /= p[j],cnt++;
			p_count[p[j]] = max(p_count[p[j]],cnt);
		}
	}

	vector<int> ans(m + 1);

	if(m == 5) ans[5] = p_count[5];
	if(m >= 3) ans[3] = p_count[3];
	if(m >= 4){
		ans[4] = p_count[2] / 2;
		if(p_count[2] % 2 == 1) ans[2] += 1;
	} else {
		ans[2] = p_count[2];
	}

	//‘«‚è‚È‚¢•ª‚ð’Ç‰Á
	int comped = accumulate(ans.begin(),ans.end(),0);
	ans[2] += n - comped;

	return ans;
}

int main(){
	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		printf("Case #%d:\n",i);
		int r; cin>>r>>n>>m>>k;
		FOR(k,r){
			auto ans = solve();
			FOR(i,sz(ans)) FOR(j,ans[i]){
				printf("%d",i);
			}
			puts("");
		}
	}
	return 0;
}
