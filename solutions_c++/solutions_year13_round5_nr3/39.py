#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

struct Edge {
    int from, to, lo, hi, pathIndex;
};

struct Pos {
public:
    /*Pos(int home):loc(home), items(0), mustgohome(false), cost(0) {
      }*/
    int loc;

    int cost;
};

class compare { // for queue
public:
	bool operator()(const Pos & a, const Pos & b) const {
		return a.cost > b.cost; // here > means lower costs go first
	}
};


class Solver {
public:
    int n;
    vector<vector<Edge> > g;
    vector<Edge> e;
    vector<int> path;
    bool canBeShortest(int len) {
	if (len <= 0)
	    return true;
	priority_queue<Pos, vector<Pos>, compare> q;
	vector<int> cost(n, 2013000000);
	vector<int> blessed(n, 0);
	cost[0] = 0;
	blessed[0] = 1;
	Pos at;
	at.loc = 0;
	at.cost = 0;
	q.push(at);

	const bool debug = false;
	if (debug) cerr << "Trying len = " << len << endl;

	vector<bool> vis(n, false);
	vis[0] = true;
	for (int i = 0; i < len; ++i) {
	    int to = e[path[i]].to;
	    if (vis[to]) return false; // one city visited twice by path
	    vis[to] = true;
	    if (i < len - 1 && to == 1) return false; // early London
	}

	do {
	    at = q.top();
	    q.pop();
	    if (at.cost > cost[at.loc]) {
		continue;
	    }
	    if (debug) cerr << "At " << at.loc << ", cost " << at.cost << ", blessed " << blessed[at.loc] << endl;
	    if (at.loc == 1) {
		return blessed[1];
	    }

	    for (int j = 0; j < g[at.loc].size(); ++j) {
		Pos p2;
		p2.loc = g[at.loc][j].to;
		int newBless = 0;
		if (blessed[at.loc] == 2 || (blessed[at.loc] == 1 && g[at.loc][j].pathIndex < len)) {
		    p2.cost = at.cost + g[at.loc][j].lo;
		    newBless = 1;
		    if (blessed[at.loc] == 2)
			newBless = 2;
		    if (g[at.loc][j].pathIndex == len - 1)
			newBless = 2;
		}
		else {
		    p2.cost = at.cost + g[at.loc][j].hi;
		}
		if (p2.cost < cost[p2.loc] || (p2.cost == cost[p2.loc] && newBless > blessed[p2.loc])) {
		    q.push(p2);
		    cost[p2.loc] = p2.cost;
		    blessed[p2.loc] = newBless;
		}
	    }

	} while (!q.empty());
	return false; // no way found at all

    }
    ret_t solve(int _n, int m, vector<Edge> _e, vector<int> _path) {
	ret_t ret;
	n = _n;
	e = _e;
	path = _path;

	for (int i = 0; i < path.size(); ++i)
	    e[path[i]].pathIndex = i;
	g = vector<vector<Edge> >(n);
	for (int i = 0; i < m; ++i) {
	    g[e[i].from].push_back(e[i]);
	}
	
	/*for (int i = 0; i <= path.size(); ++i)
	    cerr << (canBeShortest(i) ? 'T' : 'F');
	    cerr << endl;*/

	if (canBeShortest(path.size()))
	    return -1;

	int left = 1;
	int right = path.size();
	while (left < right) {
	    int mid = left + (right - left) / 2;
	    if (!canBeShortest(mid))
		right = mid;
	    else
		left = mid + 1;
	}
	ret = path[left - 1];

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
        int n, m, p;
        {
            stringstream A(s);
            A >> n >> m >> p;
        }
	vector<Edge> e(m);
	for (int i = 0; i < m; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> e[i].from >> e[i].to >> e[i].lo >> e[i].hi;
	    e[i].pathIndex = 512;
	    --e[i].from;
	    --e[i].to;
	}
	vector<int> path(p);
	getline(cin, s);
	{
	    stringstream A(s);
	    for (int i = 0; i < p; ++i) {
		A >> path[i];
		--path[i];
	    }
	}

	ret_t ret = solver.solve(n, m, e, path);

        // *** give output ***
        cout << "Case #" << no << ": ";
	if (ret >= 0)
	    cout << ret + 1<< endl;
	else
	    cout << "Looks Good To Me" << endl;
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
