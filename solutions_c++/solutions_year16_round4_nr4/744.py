#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int min_training;

void compute(int added, vector< pair<int, int> >& g) {
	bool done = true;
	for(int i = 0; i < g.size(); i++) {
		if(g[i].first != g[i].second) {
			done = false;
			break;
		}
	}
	if(done) {
		if(added < min_training) {
			min_training = added;
		}
		return;
	}

	if(g[0].first == g[0].second) {
		vector< pair<int, int> > new_g;
		for(int i = 1; i < g.size(); i++) {
			new_g.push_back(g[i]);
		}
		compute(added, new_g);
	}
	for(int i = 1; i < g.size(); i++) {
		vector< pair<int, int> > new_g;
		for(int j = 1; j < i; j++) {
			new_g.push_back(g[j]);
		}
		new_g.push_back(pair<int, int>(g[0].first + g[i].first, g[0].second + g[i].second));
		for(int j = i + 1; j < g.size(); j++) {
			new_g.push_back(g[j]);
		}
		compute(added + g[0].first * g[i].second + g[0].second * g[i].first, new_g);
	}
}

int main(int argc, char** argv) {
	int t;
	cin >> t;
	for(int iter = 0; iter < t; iter++) {
		int n;
		vector<string> l;
		cin >> n;
		l.resize(n);
		for(int i = 0; i < n; i++) {
			cin >> l[i];
		}
		vector< pair< int, int> > g;
		vector<bool> selected;
		selected.resize(n);
		int training = 0;
		for(int i = 0; i < n; i++) {
			if(selected[i]) continue;
			vector<int> q;
			q.push_back(i);
			selected[i] = true;
			int head = 0;
			while(head < q.size()) {
				int cur = q[head];
				for(int j = 0; j < n; j++) {
					if(l[cur][j] == '1') {
						for(int k = 0; k < n; k++) {
							if(!selected[k] && l[k][j] == '1') {
								q.push_back(k);
								selected[k] = true;
							}
						}
					}
				}
				head++;
			}
			set<int> machines;
			for(int j = 0; j < q.size(); j++) {
				for(int k = 0; k < n; k++) {
					if(l[q[j]][k] == '1') {
						machines.insert(k);
					}
				}
			}
			for(int j = 0; j < q.size(); j++) {
				for(set<int>::iterator it = machines.begin(); it != machines.end(); it++) {
					if(l[q[j]][*it] == '0') {
						training++;
					}
				}
			}
			g.push_back(pair<int, int>(q.size(), machines.size()));
		}
		for(int i = 0; i < n; i++) {
			bool empty = true;
			for(int j = 0; j < n; j++) {
				if(l[j][i] == '1') {
					empty = false;
					break;
				}
			}
			if(empty) {
				g.push_back(pair<int, int>(0, 1));
			}
		}
		min_training = n * n;
		compute(0, g);
		training += min_training;

		cout << "Case #" << iter + 1 << ": " << training << endl;
	}
	return 0;
}
