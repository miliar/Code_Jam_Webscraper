#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define reps(i,f,n) for(int i=f; i<int(n); ++i)
#define rep(i,n) reps(i,0,n)

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int INF = 1001001001;
const double EPS = 1e-10;

struct Seg
{
	int src, dst, p;
	bool operator< (const Seg& s)const {
		if(src != s.src)
			return src < s.src;
		else
			return dst < s.dst;
	}
};

int N;
ll f(int n)
{
	return (ll)n*N + n - (ll)n*(n+1)/2;
}

ll func(const vector<Seg>& S)
{
	vector<pii> in, out;
	rep(i, S.size()){
		in.push_back(pii(S[i].src, S[i].p));
		out.push_back(pii(S[i].dst, S[i].p));
	}
	sort(out.begin(), out.end());
	reverse(out.begin(), out.end());
	
	ll ans = 0;
	while(!in.empty()){
		vector<pii>::iterator itr
			= upper_bound(in.begin(), in.end(), pii(out.back().first, INF))-1;
		int a = itr->second;
		int b = out.back().second;
		if(a == b){
			ans += f(out.back().first - itr->first) * a;
			in.erase(itr);
			out.pop_back();
		}
		else if(a > b){
			ans += f(out.back().first - itr->first) * b;
			itr->second -= b;
			out.pop_back();
		}
		else{
			ans += f(out.back().first - itr->first) * a;
			in.erase(itr);
			out.back().second -= a;
		}
	}
	
	rep(i, S.size()){
		ans -= f(S[i].dst - S[i].src) * S[i].p;
	}
	return -ans;
}

ll solve()
{
	int n, m;
	scanf("%d%d", &n, &m);
	N = n;
	
	Seg seg[1001];
	rep(i, m){
		int a, b, p;
		scanf("%d%d%d", &a, &b, &p);
		seg[i].src = a-1;
		seg[i].dst = b-1;
		seg[i].p = p;
	}
	sort(seg, seg+m);
	seg[m].src = n+1;
	
	int most = seg[0].dst;
	vector<Seg> cand;
	ll ans = 0;
	rep(i, m+1){
		if(seg[i].src <= most){
			most = max(most, seg[i].dst);
			cand.push_back(seg[i]);
		}
		else{
			ans += func(cand);
			cand.clear();
			cand.push_back(seg[i]);
			most = seg[i].dst;
		}
	}
	
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	rep(i, t){
		printf("Case #%d: %lld\n", i+1, solve());
	}
	return 0;
}
