#include <iostream>
#include <set>

using namespace std;

int ok;
int b[100];
int p[100][100];
int t;
int r, c;
int curr;
string s;
set<int> jk;

int dec(char d) {
	if (d == '^') return 1;
	if (d == 'v') return 2;
	if (d == '<') return 3;
	if (d == '>') return 4;
	return 0;
}

int main() {
	cin >> t;
	for (int i=1;i<=t;i++) {
		curr = 0;
		cout << "Case #" << i << ": ";
		cin >> r >> c;
		for (int j= 0;j<r;j++) {
			cin >> s;
			int apu = -1;
			ok = 1;
			for (int k=0;k<c;k++) {
				if (s[k] == '^'&&(!b[k])) {
					apu = k;
					curr++;
					b[k] = 1;
					if (ok == 1) ok = 0;
					else ok = 2;
				} else if (s[k] != '.') {
					b[k] = 1;
					ok = 2;
					jk.erase(k);
				}
				p[j][k] = dec(s[k]);
			}
			if (!ok) jk.insert(apu);
		}
		for (int j=0;j<100;j++) b[j] = 0;
		if (jk.size()) {
			cout << "IMPOSSIBLE\n";
			jk.clear();
			continue;
		}
		for (int j=r-1;j>=0;j--) {
			int apu = -1;
			ok = 1;
			for (int k = 0;k<c;k++) {
				if (p[j][k] == 2 && !b[k]) {
					apu = k;
					b[k] = 1;
					curr++;
					if (ok == 1) ok = 0;
					else ok = 2;
				} else if (p[j][k]) {
					b[k] = 1;
					ok = 2;
					jk.erase(k);
				}
			}
			if (!ok) jk.insert(apu);
		}
		for (int j=0;j<100;j++) b[j] = 0;
		if (jk.size()) {
			cout << "IMPOSSIBLE\n";
			jk.clear();
			continue;
		}
		for (int k=0;k<c;k++) {
			int apu = -1;
			ok = 1;
			for (int j=0;j<r;j++) {
				if (p[j][k] == 3 && !b[j]) {
					apu = j;
					b[j] = 1;
					curr++;
					if (ok == 1) ok = 0;
					else ok = 2;
				} else if (p[j][k]) {
					b[j] = 1;
					ok = 2;
					jk.erase(j);
				}
			}
			if (!ok) jk.insert(apu);
		}
		for (int j=0;j<100;j++) b[j] = 0;
		if (jk.size()) {
			cout << "IMPOSSIBLE\n";
			jk.clear();
			continue;
		}
		for (int k = c-1;k>=0;k--) {
			int apu = -1;
			ok = 1;
			for (int j=0;j<r;j++) {
				if (p[j][k] == 4 && !b[j]) {
					b[j] = 1;
					curr++;
					apu = j;
					if (ok == 1) ok = 0;
					else ok = 2;
				} else if (p[j][k]) {
					ok = 2;
					b[j] = 1;
					jk.erase(j);
				}
			}
			if (!ok) jk.insert(apu);
		}
		for (int j=0;j<100;j++) b[j] = 0;
		if (jk.size()) {
			cout << "IMPOSSIBLE\n";
			jk.clear();
			continue;
		}
		cout << curr << "\n";
	}

}
