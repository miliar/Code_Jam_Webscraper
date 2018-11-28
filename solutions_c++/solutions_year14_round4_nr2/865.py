#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
#include <cctype>
#include <tuple>
#include <iterator>
#include <bitset>
#include <random>
#include <assert.h>
#include <unordered_map>
#include <array>

#ifdef _MSC_VER
#include <agents.h>
#endif

#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define X first
#define Y second
#define MP make_pair
#define umap unordered_map

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> P;
typedef unsigned int uint;

int main(){
	int T;
	cin >> T;
	FOR(t, 1, T + 1){
		printf("Case #%d: ", t);

		int n;
		cin >> n;
		vector<int> v(n);
		rep(i, n) cin >> v[i];

		vector<int> a = v;
		sort(ALL(a));
		rep(i, n) v[i] = lower_bound(ALL(a), v[i]) - a.begin() + 1;
		vector<int> idx(n+1);
		rep(i, n) idx[v[i]] = i;

		int ans = 0;
		int l = 0, r = n-1;
		rep(j, n){
			int pos = idx[j + 1];
			if (r - pos < pos - l){
				for (int i = pos; i < r; ++i){
					swap(v[i], v[i + 1]);
					swap(idx[v[i]], idx[v[i + 1]]);
					++ans;
				}
				--r;
			}
			else{
				for (int i = pos; i > l; --i){
					swap(v[i], v[i - 1]);
					swap(idx[v[i]], idx[v[i - 1]]);
					++ans;
				}
				++l;
			}
		}

		cout << ans << endl;
	}


	return 0;
}