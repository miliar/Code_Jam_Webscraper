#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef string ret_t;

class Solver {
public:
    int n, m;
    vector<vector<int> > adj;
    vector<bool> vis;
    void dfs(int at) {
	if (vis[at])
	    return;
	vis[at] = true;
	for (int j = 0; j < adj[at].size(); ++j)
	    dfs(adj[at][j]);
    }
    bool pos(vector<int> reach) {
	vis = vector<bool>(n, false);
	int start = 0;
	for (int i = 0; i < n; ++i) {
	    if (reach[i] == -2)
		vis[i] = true;
	    if (reach[i] == 0)
		start = i;
	}
	dfs(start);
	for (int i = 0; i < n; ++i)
	    if (!vis[i])
		return false;
	return true;
    }
    ret_t solve(vector<string> c, vector<pair<int, int> > e, int _n, int _m) {
	n = _n;
	m = _m;
	adj = vector<vector<int> >(n);
	for (int i = 0; i < m; ++i) {
	    adj[e[i].first - 1].push_back(e[i].second - 1);
	    adj[e[i].second - 1].push_back(e[i].first - 1);
	}

	ret_t ret;
	vector<int> reach(n, -1);
	ret = c[0];
	int cur = 0;
	for (int i = 1; i < n; ++i)
	    if (c[i] < ret)
		ret = c[i], cur = i;
	reach[cur] = 0;
	int numvis = 1;
	//cerr << "  Start\t" << cur << endl;
	while (numvis < n) {
	    vector<pair<string, int> > cand;
	    for (int i = 0; i < n; ++i)
		if (reach[i] == -1)
		    cand.push_back(make_pair(c[i], i));
	    sort(cand.begin(), cand.end());
	    for (int j = 0; j < cand.size(); ++j) {
		int to = cand[j].second;
		//cerr << "  Try:\t" << to;
		int from = -1;
		int fromreach = -1;
		for (int k = 0; k < adj[to].size(); ++k) {
		    int here = adj[to][k];
		    if (reach[here] < 0) continue;
		    if (reach[here] < fromreach) continue;
		    from = here;
		    fromreach = reach[here];
		}
		if (from < 0) {
		    //cerr << "\tUnreachable" << endl;
		    continue;
		}
		vector<int> reach2(reach);
		for (int i = 0; i < n; ++i) {
		    if (reach2[i] > fromreach)
			reach2[i] = -2;
		}
		reach2[to] = fromreach + 1;
		if (pos(reach2)) {
		    //cerr << "\tSucces - from " << from << endl;
		    ++numvis;
		    ret += c[to];
		    reach = reach2;
		    break;
		}
		else {
		    //cerr << "\tImpossible" << endl;
		}
	    }
	}
	return ret;
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
	int n, m;
        {
            stringstream A(s);
            A >> n >> m;
        }
	vector<string> c(n);
	vector<pair<int, int> > e(m);
	for (int i = 0; i < n; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> c[i];
	}
	for (int i = 0; i < m; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> e[i].first >> e[i].second;
	}
        ret_t ret = solver.solve(c, e, n, m);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
