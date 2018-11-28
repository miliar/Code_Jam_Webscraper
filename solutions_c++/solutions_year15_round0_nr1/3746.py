#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

vector < int > a;
int T, n, x;

int main()
{
	freopen("large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		cin >> n;
		int ans = 0;
		int s = 0;
		getc(stdin);
		
		for (int i = 0; i < n + 1; i++) {
			//~ cout << char(getc(stdin)) << ' ';
			x = getc(stdin) - '0';
			//~ cout << x << endl;
			ans = max(ans, i - s);
			s += x;
		}
		//~ cout << endl;
		printf("Case #%d: %d\n", t + 1, ans);
	}
}
