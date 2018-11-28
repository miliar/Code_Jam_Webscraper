#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct block {
	double w;
	char c;
	bool used;
};

bool comp(const block& a, const block& b) {
	if (a.w < b.w) return true;
	return false;
}

int main() {
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";
		int n;
		cin >> n;
		vector<block> v;
		for (int i=0; i<n; i++) {
			block b;
			cin >> b.w;
			b.c = 'n';
			b.used = false;
			v.push_back(b);
		}
		for (int i=0; i<n; i++) {
			block b;
			cin >> b.w;
			b.c = 'k';
			b.used = false;
			v.push_back(b);
		}
		sort(v.begin(),v.end(),comp);
		int old,nou;
		old = nou = 0;
		for (int i=0; i<v.size(); i++) {
			if (v[i].c == 'n') continue;
			for (int j=i+1; j<v.size(); j++) {
				if (v[j].c == 'n' and !v[j].used) {
					nou++;
					v[j].used = true;
					break;
				}
			}
		}	
		for (int i=0; i<v.size(); i++) v[i].used = false;
		for (int i=0; i<v.size(); i++) {
			if (v[i].c == 'k') continue;
			for (int j=i+1; j<v.size(); j++) {
				if (v[j].c == 'k' and !v[j].used) {
					old++;
					v[j].used = true;
					break;
				}
			}
		}
		old = n-old;
		cout << nou << ' ' << old << endl;
	}
}
