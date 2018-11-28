#include <fstream>
using namespace std;

int main() {
	ifstream f("data.in");
	freopen("data.out", "w", stdout);

	int T;
	f >> T;
	for(int test = 1; test <= T; ++test) {
		int N;
		char s[1007];
		
		f >> N >> s;
		
		int cnt = 0, ans = 0;
		for(int i = 0; i <= N; ++i) {
			if(cnt < i) {
				int t = i - cnt;
				ans += t;
				cnt += t;
			}
			cnt += s[i] - '0';
		}
		
		printf("Case #%d: %d\n", test, ans);
	}

	f.close();
	fclose(stdin);

	return 0;
}
