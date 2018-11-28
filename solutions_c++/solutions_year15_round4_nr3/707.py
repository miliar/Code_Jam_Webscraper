#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

int lang[100000];
map<string,int> convert;
vector<int> words[250];

// 1 = english, 2 = french, 3 = both

void solve()
{
	convert.clear();
	int n;
	cin >> n;
	string sent;
	getline(cin,sent);
	int uid = 0;
	for (int i=0; i<n; i++) {
		getline(cin, sent);
		stringstream ss(sent);
		words[i].clear();
		string word;
		while (ss >> word) {
			if (convert.find(word) == convert.end()) convert[word] = ++uid;
			words[i].push_back(convert[word]);
		}
	}
	int best = 1000000000;
	int L = (1<<(n-2));
	for (int b=0; b<=L; ++b) {
		//cout << b << endl;
		int conflicts = 0;
		fill_n(lang, uid+1, 0);
		for (int w : words[0]) lang[w] = 1;
		for (int w : words[1]) {
			int x = lang[w];
			if (x == 0) lang[w] = 2;
			else if (x == 1) {
				lang[w] = 3;
				conflicts++;
				//cout << "Word conflict: " << w << endl;
			}
		}
		for (int i=2; i<n; i++) {
			bool eng = (b & (1 << (i-2))) != 0;
			int ml = eng ? 1 : 2;
			for (int w : words[i]) {
				int x = lang[w];
				if (x == 0) lang[w] = ml;
				else if (x == 3 - ml) {
					lang[w] = 3;
					conflicts++;
					//cout << "Word conflict: " << w << endl;
				}
			}
		}
		best = min(conflicts, best);
	}
	cout << best;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for (int tn=1; tn<=t; tn++) {
		cout << "Case #" << tn << ": ";
		solve();
		cout << endl;
	}
	return 0;
}