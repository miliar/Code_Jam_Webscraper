#include<iostream> 
#include<cstdio> 
#include<cmath> 
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<ctime>
#include<cassert>
#include<queue>

#define LL long long
#define mp make_pair
#define f first
#define s second
#define pii pair<int, int>
#define pb push_back

using namespace std;

const LL M = 1e7 + 5;
int t;

bool check (LL x)
{
	vector<int> s;
	while(x) {
		s.pb(x % 10);
		x /= 10;
	}
	for (int i = 0; i * 2 < s.size(); i++)
		if (s[i] != s[s.size() - 1 - i])
			return false;
	return true;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen(".out", "w", stdout);

	cin >> t;

	vector<LL> ans;

	for (LL i = 1; i < M; i++)
		if (check(i) && check(i * i)) {
			ans.pb(i * i);
//			cerr << i << ' ' << i * i << endl;
		}

	for (int test = 0; test < t; test++) {
		LL a, b;
		cin >> a >> b;

		LL cnt = 0;
		for (int i = 0; i < ans.size(); i++) {
			if (ans[i] > b)
				break;
			if (ans[i] >= a)
				cnt++;
		}

		cout << "Case #" << test + 1 << ": " << cnt << endl;
	}

	return 0;
}