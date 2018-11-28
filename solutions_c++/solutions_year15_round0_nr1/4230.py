#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;


int main() {

	ofstream cout("out.txt");
	ifstream cin("in.in");
	int T;
	cin >> T;
	for(int idx = 1; idx <= T; idx++) {
		int n;
		string s;
		cin >> n >> s;
		int numsofar = s[0] - '0';
		int ans = 0;
		for (int i = 1; i < s.size(); i++) {
			if (i > numsofar) {
				ans += i - numsofar;
				numsofar = i;
			}
			numsofar += s[i] - '0';
		}
		cout << "Case #" << idx << ": " << ans << endl;
	}
	return 0;
}