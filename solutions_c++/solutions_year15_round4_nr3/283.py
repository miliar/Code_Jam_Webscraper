#include <bits/stdc++.h>
using namespace std;

char line[1111111];

unordered_map<string, int> ids;
int counter = 0;

int getid(const string& s) {
	if (ids.count(s)) return ids[s];
	return ids[s] = counter++;
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
	
	int T;
	cin >> T;
	for (int __it = 1; __it <= T; ++__it) {
		int n;

		ids.clear();
		counter = 0;

		scanf("%d\n", &n);
		vector< vector<int> > a(n);
		for (int i = 0; i < n; ++i) {
			gets(line);
			istringstream s(line);
			string word;
			while (s >> word) {
				a[i].push_back( getid(word) );
			}
		}

		int ans = counter;
		vector<char> mask;
		for (int i = 0; i < (1 << (n - 2)); ++i) {
			mask.assign(counter, 0);
			for (int j = 0; j < n; ++j) {
				int l;
				if (j == 0) l = 0;else
				if (j == 1) l = 1;else l = ((i & (1 << (j - 2))) > 0);

				l = 1 << l;

				for (int k = 0; k < a[j].size(); ++k)
					mask[ a[j][k] ] |= l;
			}
			int subans = 0;
			for (int j = 0; j < counter; ++j) 
				if (mask[j] == 3)
					++subans;
			ans = min(ans, subans);					
		}

		cout << "Case #" << __it << ": " << ans << endl;			
		cerr << __it << " " << clock() << endl;
	}
    
    return 0;
}
