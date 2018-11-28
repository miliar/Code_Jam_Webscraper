#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main() {
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int n;
		string str;
		cin >> n;
		cin >> str;
		int ans = 0;
		int c = 0;
		for (int i = 0 ; i < str.length() ; i++) {
			if(str[i] != '0' && i > c) {
				ans = ans + i - c;
				c = i;
			}
			c = c + str[i] - '0';
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
