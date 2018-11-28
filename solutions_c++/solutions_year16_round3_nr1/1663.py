#include <iostream>
#include <fstream>
#include <bitset>
#define LL long long
#define DN 30

using namespace std;

int p[DN], n;

int is_valid() {
	int maxx = 0, sum = 0;
	for(int i = 0; i < n; ++i) {
		if(p[i] > maxx)
			maxx = p[i];
		sum += maxx;
	}
	if(maxx > sum / 2)
		return 0;
	return 1;
}

int take_one() {
	int maxx = 0, index = -1;
	for(int i = 0; i < n; ++i) {
		if(p[i] > maxx) {
			maxx = p[i];
			index = i;
		}
	}
	return index;
}

int main() {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tst = 1; tst <= t; ++tst) {
		cin >> n;
		for(int i = 0; i < n; ++i)
			cin >> p[i];
		cout << "Case #" << tst << ": ";
		int ok = 1;
		while(ok) {
			int index = take_one();
			if(index == -1)
				break;
			p[index]--;
			char c = 'A' + index;
			cout << c;
			if(is_valid()) {
				int index = take_one();
				p[index] --;
				if(is_valid()) {
					c = 'A' + index;
					cout << c;
				}
				else
					p[index] ++;
			} else {
				index = take_one();
				p[index] --;
				c = 'A' + index;
				cout << c;
			}
			cout << " ";
		}
		cout << '\n';
	}
	return 0;
}