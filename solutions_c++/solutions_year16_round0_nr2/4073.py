#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

void work(int p)
{
	string s;
	cin >> s;
	s = ' '+s;
	int cnt = 0;
	for(int i = 1; i < (int)s.size(); ++i) {
		if(s[i] != s[i-1]) {
			++cnt;
		}
	}
	if(s[(int)s.size()-1] == '+') {
		--cnt;
	}
	cout << "Case #" << p << ": " << cnt << endl;
}

int main()
{
	#define LOCAL_
	#ifdef LOCAL
	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);
	#endif

	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i) {
		work(i);
	}
	return 0;
}
