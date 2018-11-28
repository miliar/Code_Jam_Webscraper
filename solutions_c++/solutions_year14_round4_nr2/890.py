#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define len(x) ((int) (x).size())
#define endl '\n'

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif

using namespace std;

typedef long long int64;
typedef long double ld;
typedef unsigned long long lint;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);
const int N = 1e5;

int n;
int a[N], p[N], s[N];

inline void solve(){
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	for (int i = 0; i < n; i++)
		p[i] = i;
	int ans = inf;
	do{
		for (int i = 0; i < n; i++)
			s[i] = a[p[i]];
		int index = max_element(s, s + n) - s;
		bool cool = true;
		for (int i = 0; i < index; i++)
			if (s[i] >= s[i + 1]){
				cool = false;
				break;
			}
		if (!cool)
			continue;
		for (int i = index; i < n - 1; i++)
			if (s[i] <= s[i + 1]){
				cool = false;
				break;
			}
		if (!cool)
			continue;
		int sum = 0;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (p[i] > p[j])
					sum++;
		ans = min(ans, sum);
	}
	while (next_permutation(p, p + n));
	printf("%d\n", ans);
}

int main(){
#if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif
	int t; cin >> t;
	for (int i = 0; i < t; i++){
		printf("Case #%d: ", i + 1);
		solve();
		eprintf("%d\n", i + 1);
	}
    return 0;
}
