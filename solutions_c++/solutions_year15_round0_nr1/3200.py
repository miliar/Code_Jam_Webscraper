#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int s;
		string str;
		cin >> s >> str;
		int res = 0;
		int stand = 0;
		for(int i = 0; i < str.size(); i++) {
			if(stand < i) {
				res += i - stand;
				stand = i;
			}
			stand += str[i] - '0';
		}

		cout << "Case #"  << t+1 << ": " << res << endl;
	}
	return 0;
}
