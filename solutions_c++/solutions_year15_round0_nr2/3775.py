#include <cstring>
#include <map>
#include <numeric>
#include <sstream>
#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <queue>
#include <string>
#include <cctype>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb(x) push_back((x))
#define REP(i,x,y) for(int i = x; i < int(y); i++)
#define FOR(it,A) for(typeof (A.begin()) it = A.begin(); it!= A.end(); it++)
#define CUA(x) (x) * (x)
#define mp(x,y) make_pair((x),(y))
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
#define I (1LL << 40)
#define sz size()
#define oo (1<<30)
#define EPS (1e-9)

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<pii> vii;
typedef vector<string> vs;
typedef vector<int> vi;

int solve3(int d, vi arr){
	int mxsec=-1;
	REP(i,0,d) mxsec = max(mxsec, arr[i]);
	int mnsec = mxsec ;

	for(int i=1;i<=mxsec;i++){
		int sum=i;

		for(int j=0;j<d;j++)
		{
			if( arr[j] > i )
			{
				if( arr[j]%i == 0 )
					sum += (arr[j]/i-1) ;

				else
					sum += (arr[j]/i) ;

			}
		}
		mnsec = min(mnsec,sum) ;

	}
    return mnsec;
}
int dp(vi v){

	bool f1 = true, f2 = true;
	REP(i, 2, v.size()) if(v[i]>0) f1 = false;
	if(v[1]>0) f2 = false;
	if(f1){
		if(f2) return 0;
		return 1;
	}
	int ind;
	for(int i = v.size()-1; i > 0; i--)
		if(v[i] > 0){
			ind = i;
			break;
		}
	v[ind/2]++;
	v[(ind+1)/2]++;
	v[ind]--;
	int ret2 = dp(v);

	v[ind/2]--;
	v[(ind+1)/2]--;
	v[ind]++;

	REP(i,0,9) v[i] = v[i+1];
	v[9] = 0;
	int ret1 = dp(v);

	return min(1 + ret1,1 + ret2);
}

int solve2(int n, vi v){
	vi aa(10);
	REP(i, 0, n) aa[v[i]]++;
	int ret = dp(aa);
	return ret;
}
int solve(int n, vi v){
	int ans = 0;
	int resp = 1000000000;
	priority_queue<int> pq;
	REP(i, 0, n) pq.push(v[i]);
	while(pq.top() > 3){
		int mx = pq.top();
		resp = min(resp, mx + ans);
		pq.pop();
		pq.push(mx/2);
		pq.push((mx+1)/2);
		ans++;
	}
	ans += pq.top();
	resp = min(resp, ans);
	return resp;
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif	
	int T, N;
	cin >> T;
	REP(i, 0, T){
		cin >> N;
		vi P(N);
		REP(j, 0, N){
			cin >> P[j];
		}
		cout << "Case #" << i+1 << ": " << solve3(N, P) << endl;
	}
		
	return 0;
}





