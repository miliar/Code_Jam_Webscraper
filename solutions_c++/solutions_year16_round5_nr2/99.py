#include <iostream>
#include <random>
#include <iomanip>
#include <cassert>

using namespace std;

mt19937 rng;

int n;
int p[128];
string l;
int m;
string w[16];

bool seen[128];
vector<int> ord;
string text;

void dfs(int c) {
	if(seen[c]) return;
	seen[c] = true;
	if(p[c] != -1) dfs(p[c]);
	ord.push_back(c);
	text.push_back(l[c]);
}

int main() {
	int tc;
	cin >> tc;
	
	for(int ti = 1; ti <= tc; ++ti) {
		cin >> n;
		for(int i = 0; i < n; ++i) {
			cin >> p[i];
			--p[i];
		}
		cin >> l;
		cin >> m;
		for(int i = 0; i < m; ++i) {
			cin >> w[i];
		}
		
		fill(seen, seen + n, false);
		ord.clear();
		text.clear();
		
		for(int i = 0; i < n; ++i) {
			dfs(i);
		}
		
		assert(ord.size() == n);
		assert(text.size() == n);
		
		int wc[16];
		fill(wc, wc + 16, 0);
		
		int ac = 30000;
		for(int ai = -ac / 10; ai < ac; ++ai) {
			for(int ij = 0; ij < 1000; ++ij) {
				if((rng() & 7) && n >= 2) {
					int i = uniform_int_distribution<int>(0, n - 2)(rng);
					if(p[ord[i]] != ord[i + 1] && p[ord[i + 1]] != ord[i]) {
						swap(ord[i], ord[i + 1]);
						swap(text[i], text[i + 1]);
					}
				}
			}
			
			if(ai >= 0) {
				for(int i = 0; i < m; ++i) {
					if(text.find(w[i]) != text.npos) {
						++wc[i];
					}
				}
			}
		}
		
		cout << "Case #" << ti << ":";
		for(int i = 0; i < m; ++i) {
			cout << ' ' << fixed << setprecision(4) << (double)wc[i] / (double)ac;
		}
		cout << '\n';
	}
	
	return 0;
}
