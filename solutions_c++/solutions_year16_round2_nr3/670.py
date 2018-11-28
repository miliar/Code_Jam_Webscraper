#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Matching {
public:
    vector<vector<bool> > g;
    vector <bool> used;
    vector<int> fromMatch, toMatch;
    int n, m, ret;

    bool dfs(int from) {
        if (used[from]) return false;
        //cout << "dfs at " << from << endl;
        used[from] = true;
        for (int to = 0; to < m; ++to) {
            if (g[from][to]) {
                if (toMatch[to] == -1 || dfs(toMatch[to])) {
                    fromMatch[from] = to;
                    toMatch[to] = from;
                    return true;
                }
            }
        }
        //cout << "No path" << endl;
        return false;
    }
    int maxmatch(vector<vector<bool> > & g_) {
        // create g with: vector<vector<bool> > g(n, vector<bool>(m, false));
        g = g_;
        n = g.size(); // number of from nodes
        if (n == 0) return 0;
        m = g[0].size(); // number of to nodes
        ret = 0;
        fromMatch = vector<int>(n, -1);
        toMatch = vector<int>(m, -1);
        used = vector<bool>(n, false);
        for (int source = 0; source < n; ++source) {
            if (dfs(source)) {
                ++ret;
            }
            used = vector<bool>(n, false);
        }
        return ret;
    }
};

class Solver {
public:
    ret_t solve(int nE, vector<string> w1, vector<string> w2) {
        map<string, int> m1;
        map<string, int> m2;
        int nV1 = 0;
        int nV2 = 0;
        vector<int> v1(nE);
        vector<int> v2(nE);
        for (int i = 0; i < nE; ++i) {
            map<string, int>::iterator it1 = m1.find(w1[i]);
            if (it1 == m1.end()) {
                v1[i] = m1[w1[i]] = nV1++;
            }
            else {
                v1[i] = m1[w1[i]];
            }
            map<string, int>::iterator it2 = m2.find(w2[i]);
            if (it2 == m2.end()) {
                v2[i] = m2[w2[i]] = nV2++;
            }
            else {
                v2[i] = m2[w2[i]];
            }
        }
        vector<vector<bool> > g(nV1, vector<bool>(nV2, false));
        for (int i = 0; i < nE; ++i) {
            g[v1[i]][v2[i]] = true;
        }
        Matching M;
        ret_t ret;
        ret = M.maxmatch(g) + nE - nV1 - nV2;
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
        cerr //<< "Case "
            << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int nE;
        {
            stringstream A(s);
            A >> nE;
        }
        vector<string> w1(nE);
        vector<string> w2(nE);
        for (int i = 0; i < nE; ++i) {
            getline(cin, s);
            stringstream A(s);
            A >> w1[i] >> w2[i];
        }
        ret_t ret = solver.solve(nE, w1, w2);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
