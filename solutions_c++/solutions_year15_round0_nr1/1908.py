#include <cstring>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;

	for(int z = 1; z <= t; z++) {
		int s;
		cin >> s;
		string d;
		cin >> d;

		int cnt = d[0]-'0';
		int ret = 0;

		for(int i = 1; i <= s; i++) {
			int tmp = d[i]-'0';

			if(i <= cnt) cnt += tmp;
			else {
				int diff = (i-cnt);
				ret += diff;
				cnt += (diff+tmp);
			}
		}

		cout << "Case #" << z << ": " << ret << endl;
	}
}

