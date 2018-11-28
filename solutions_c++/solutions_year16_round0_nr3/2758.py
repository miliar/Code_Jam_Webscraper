/*/**/

#include <bits/stdc++.h>

using namespace std;

vector < vector < long long > > v;
vector < long long > ans;

int main() {
//	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int found = 0;
	for(long long mask = 0; mask < (1ll << 14) and found < 50; mask++) {
		long long num = (1ll << 15) | 1;
		num |= (mask << 1);
		int bad = 0;
		vector < long long > temp;
		for(int base = 2; base <= 10; base++) {
			bad = 0;
			long long now = 0;
			long long b = 1;
			long long foo = num;
			while(foo) {
				now += b * (foo & 1);
				foo >>= 1;
				b *= base;
			}
			for(long long i = 2; i * i <= now; i++) {
				if(now % i == 0) {
					temp.push_back(i);
					bad = 1;
					break;
				}
			}
			if(not bad) {
				break;
			}
		}
		if(bad) {
			ans.push_back(num);
			v.push_back(temp);
			found++;
		}
	}
	cout << "Case #1:" << endl;
	for(int i = 0; i < ans.size(); i++) {
		vector < int > b;
		long long num = ans[i];
		while(num) {
			b.push_back(num & 1);
			num >>= 1;
		}
		reverse(b.begin(), b.end());
		for(int j = 0; j < b.size(); j++) {
			cout << b[j];
		}
		for(int j = 0; j < v[i].size(); j++) {
			cout << " " << v[i][j];
		}
		cout << endl;
	}
	return 0;
}

