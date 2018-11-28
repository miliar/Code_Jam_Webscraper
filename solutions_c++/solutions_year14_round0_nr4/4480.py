#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>

typedef long long LL;
#define pb push_back
#define MPII make_pair<int, int>
#define PII pair<int, int>
#define sz(x) (int)x.size()

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

const int maxn = 2000;
int n;
double a[maxn], b[maxn];

int Solve1(){
	for (int i = 0; i <= n; ++i){
		bool ok = true;
		for (int j = i + 1; j <= n; ++j)
			if (a[j] < b[j - i]){
				ok = false;
				break;
			}
		if (ok) return n - i;
	}
}

int Solve2(){
	set<double> S;
	S.clear();
	for (int i = 1; i <= n; ++i) S.insert(b[i]);
	int sum = 0;
	for (int i = 1; i <= n; ++i){
		set<double>::iterator iter = S.lower_bound(a[i]);
		if (iter == S.end()){
			S.erase(S.begin());
			++sum;
		}else S.erase(iter);
	}
	return sum;
}

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Cases = 1; Cases <= T; ++Cases){
		printf("Case #%d: ", Cases);
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%lf", &a[i]);
		for (int i = 1; i <= n; ++i)
			scanf("%lf", &b[i]);
		sort(a + 1, a + 1 + n);
		sort(b + 1, b + 1 + n);
		printf("%d %d\n", Solve1(), Solve2());
	}
	return 0;
}

