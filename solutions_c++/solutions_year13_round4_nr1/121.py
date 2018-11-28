#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef int ret_t;
typedef long long ll;
const ll MOD = 1000002013;
struct Trav {
    ll from;
    ll to;
    ll num;
};
struct Pers {
    Pers(ll _from, ll _num) {from = _from; num = _num;}
    ll from;
    ll num;
};

class Solver {
public:
    ll cost(ll d, ll N) {
	return (d * N - d * (d - 1) / 2) % MOD;
    }
    ret_t solve(ll N, int M, vector<Trav> g) {
	ll should, ret;
	should = ret = 0;
	for (int i = 0; i < M; ++i) {
	    ll d = g[i].to - g[i].from;
	    should += g[i].num * cost(d, N);
	    should %= MOD;
	}

	ll cur = -1;
	ll next = -1;
	stack<Pers> S;
	while (true) {
	    next = N + 1;
	    for (int i = 0; i < M; ++i) {
		if (g[i].from > cur) next = min(next, g[i].from);
		if (g[i].to > cur) next = min(next, g[i].to);
	    }
	    if (next > N)
		break;
	    ll in = 0;
	    ll out = 0;
	    for (int i = 0; i < M; ++i) {
		if (g[i].from == next) in += g[i].num;
		if (g[i].to == next) out += g[i].num;
	    }

	    S.push(Pers(next, in));

	    while (out > 0) {
		ll here = min(out, S.top().num);
		ll from = S.top().from;
		out -= here;
		S.top().num -= here;
		if (S.top().num == 0) S.pop();
		ret += here * cost(next - from, N);
		ret %= MOD;
	    }

	    cur = next;
	}

	ll loss = should - ret;
	int ret2 = (loss % MOD + MOD) % MOD;
	return ret2;
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
	vector<Trav> g(m);
	for (int i = 0; i < m; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> g[i].from >> g[i].to >> g[i].num;
	}
        ret_t ret = solver.solve(n, m, g);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
