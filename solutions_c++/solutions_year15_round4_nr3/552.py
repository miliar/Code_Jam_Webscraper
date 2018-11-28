#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
using namespace std;

#define	pb						push_back
#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))
#define	all(v)					(v).begin(),(v).end()

inline void check(vector<bool> &t, const vector<int> &d)
{
	rep(i, d.size())
		t[d[i]] = true;
}

int solve()
{
	int N;

	cin >> N;

	map<string, int> table;
	vector<vector<int>> sentences;
	string tmp;
	getline(cin, tmp);
	rep(i, N) {
		getline(cin, tmp);
		stringstream ss(tmp);
		string word;
		vector<int> sent;
		while(ss >> word) {
			int id;
			map<string, int>::iterator it = table.find(word);
			if(it == table.end()) {
				id = table.size();
				table[word] = id;
			} else {
				id = it->second;
			}
			sent.pb(id);
		}
		sentences.pb(sent);
	}

	vector<bool> english(table.size());
	vector<bool> french(table.size());

	check(english, sentences[0]);
	check(french, sentences[1]);

	int result = 1 << 29;
	rep(i, 1 << (N - 2)) {
		vector<bool> ten = english;
		vector<bool> tfr = french;

		rep(j, N - 2) {
			if(i & (1 << j))
				check(ten, sentences[j+2]);
			else
				check(tfr, sentences[j+2]);
		}

		int tres = 0;
		rep(j, table.size())
			if(ten[j] && tfr[j])
				++tres;
		result = min(result, tres);
	}

	return result;
}

int main()
{
	int T;

	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
