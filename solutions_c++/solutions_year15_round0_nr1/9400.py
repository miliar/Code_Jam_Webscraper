#include <iostream>
using namespace std;

int T;
int S;
int s[1002];
char c;
int main() {
	cin >> T;
	int t = 0;
	while(t++ < T) {
		cin >> S;
		int ans = 0;
		int psum = 0;
		for(int i = 0; i < S + 1; ++i) {
			cin >> c;
			s[i] = c - '0';
			if(psum >= i) {
				psum += s[i];
			} else {
				ans += i - psum;
				psum = i;
				psum += s[i];
			}
		}
		cout << "Case #" << t << ": " << ans << endl;

	}
}
