#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int smax;
char s[1000];

void solve(){
	scanf("%d %s", &smax, &s);

	int st = 0, res = 0;
	for (int i = 0; i <= smax; ++ i) {

		if (s[i] == '0') continue;
		if (st >= i) {
			st += (s[i] - '0');
		} else {
			int need = i - st;
			res += i - st;
			st += (s[i] - '0') + need;
		}
		// cout << st << ",";
	}
	cout << res;
}

int N;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> N;
	for (int i = 0; i < N; ++ i) {
		printf("Case #%d: ", i + 1);
		solve();
		cout << endl;
	}
	fclose(stdout);
	return 0;
}