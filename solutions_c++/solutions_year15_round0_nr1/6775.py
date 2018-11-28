#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
//	ifstream cin("ovation.in");
//	ofstream cout("ovation.out");
	int t,n;
	cin >> t;
	string audience;
	for(int i(1); i <= t; ++i) {
		cin >> n >> audience;
		int people = audience[0]-'0',
			extras = 0;
		for(int j(1); j <= n; ++j) {
			int level = audience[j] - '0';
			if(j > people) {
				extras += j-people;
				people += j-people;
			}
			people += level;
		}
		cout << "Case #" << i << ": " << extras << "\n";
	}
    return 0;
}
