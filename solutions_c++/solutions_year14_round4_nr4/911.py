#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int T, Sn, N;
set<vector<set<string> > > nodecache;

vector<int> lst;
vector<string> perm;

int findtotalnodes() {
	int numnodes=0, start=0,end=0;
	for (int eles : lst) {
		set<string> nodes, strings;
		end += eles;
		for (int i = start; i < end; i++) {
			string const& s = perm[i];
			strings.insert(s);
			for (unsigned int j = 0; j <= s.length(); j++) {
				nodes.insert(s.substr(0, j));
			}
		}
		numnodes += nodes.size();
		numnodes %= 1000000007;
		start = end;
	}
	return numnodes;
}

int maxnodes, maxnodesways;
void proc(int n) {
	if (int(lst.size()) == N) {
		int total = 0;
		for (int i : lst) total += i;
		if (total != Sn) return;
		
		// now we have a list of assignments
		// lst[n] = number of strings in server n
		do {
			vector<set<string> > cacheentry;
			int start=0,end=0;
			for (int eles : lst) {
				set<string> strings;
				end += eles;
				for (int i = start; i < end; i++) {
					strings.insert(perm[i]);
				}
				cacheentry.push_back(strings);
				start = end;
			}
			if (nodecache.count(cacheentry) != 0) continue;
			nodecache.insert(cacheentry);

			int totalnodes = findtotalnodes();
			/*if (totalnodes == 10) {
				int start=0,end=0;
				for (int eles : lst) {
					end += eles;
					for (int i = start; i < end; i++) {
						string const& s = perm[i];
						cout << s << ' ';
					}
					cout << endl;
					start = end;
				}
				cout << endl;
			}*/
			if (totalnodes > maxnodes) {
				maxnodes = totalnodes;
				maxnodesways = 1;
			} else if (totalnodes == maxnodes) {
				maxnodesways++;
			}
		} while (next_permutation(begin(perm), end(perm)));
		return;
	}
	for (int i = 1; i <= Sn; i++) {
		lst.push_back(i);
		proc(n+1);
		lst.pop_back();
	}
}

int main() {
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> Sn >> N;
		maxnodes = -1;
		perm.resize(Sn);
		for (int i = 0; i < Sn; i++) cin >> perm[i];
		sort(begin(perm), end(perm));
		proc(0);
		cout << "Case #" << tc << ": " << maxnodes << ' ' << maxnodesways << endl;
	}
}
