#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]){
	int T; cin >> T;
	for (int c = 1; c <= T; ++c) {
		int S, cnt = 0, ans = 0;
		string aud;
		cin >> S >> aud;
		for (int i = 0; i <= S; ++i) {
			if (cnt < i) {
				ans += i - cnt;
				cnt += i - cnt;
			}
			cnt += aud[i] - '0';
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}