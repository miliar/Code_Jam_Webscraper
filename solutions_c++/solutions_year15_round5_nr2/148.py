#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;
const int maxn = 500050;

LL a[maxn];
string s[maxn];
int n;
LL sum[2000];
LL l[2000], r[2000];
int k;

void solve() {
	LL ans = 0;
	LL slack = 0;
	LL best = -1;
	LL mov = 0;
	int bas;
	cin >> n >> k;
	for (int i = 1; i <= n-k+1; ++i ) cin >> sum[i];
	for (int i = 1; i <= k; ++i ) {
		LL tmp = 0;
		l[i] = r[i] = 0;
		for (int j = i; j+1 <= n-k+1; j += k ) {
			tmp += sum[j+1] - sum[j];
			//cout << tmp << endl;
			l[i] = min(l[i], tmp);
			r[i] = max(r[i], tmp);
		}
	}
	for (int i = 1; i <= k; ++i ) {
		if (r[i]-l[i]>best) {
			best = r[i]-l[i];
			bas = i;
		}
	}
	//cout << best << endl;
	for (int i = 1; i <= k; ++i ) {
		mov += l[bas] - l[i];
		slack += best - (r[i]-l[i]);
	}
	mov %= k;
	if (mov < 0) mov += k;
	LL left = (sum[1]-mov) % k;
	if (left < 0) left += k;
	if (slack <left) ans = best+1;
	else ans = best;
	cout << ans;
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int caseNum;
	cin >> caseNum;
	for (int caseID = 1; caseID <= caseNum; ++caseID) {
		cout << "Case #" << caseID << ": ";
		solve(); 
		cout << endl;
		fflush(stdout);
		cerr << "Case #" << caseID << " | " << caseNum << endl;
	}
}