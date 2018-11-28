#define _USE_32BIT_TIME_T 1
#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

const int Z = 1000000007;

int worst, cnt;

void doit(int cur, int N, const vector<string>& v, vector<int>& x)
{
    if (cur == v.size()) {
        vector<unordered_set<string> > V(N);
        //vector<set<string> > V(N);
        for (int j = 0; j < x.size(); ++j) {
            for (int i = 1; i <= v[j].size(); ++i) {
                V[x[j]].insert(v[j].substr(0, i));
            }
        }
        int amt = 0;
        for (int i = 0; i < V.size(); ++i) {
            if (!V[i].empty())
                amt+= V[i].size() + 1;
        }
        if (amt == worst)
            ++cnt;
        else if (amt > worst) {
            /*DEBUG(amt);
            for (int i = 0; i < x.size(); ++i) {
                cout << x[i] << " ";
            }
            for (int i = 0; i < V.size(); ++i) {
                DEBUG(i);
                vector<string> v0(V[i].begin(), V[i].end());
                for (int j = 0; j < v0.size(); ++j) {
                    cout << v0[j] << endl;
                }
            }*/
            worst = amt;
            cnt = 1;
        }
    } else {
        for (int j = 0; j < N; ++j) {
            x[cur] = j;
            doit(cur + 1, N, v, x);
        }
    }
}

string result(int N, const vector<string>& v)
{
    worst = cnt = 0;
    vector<int> x(v.size());
    doit(0, N, v, x);
    char buf[1000];
    sprintf(buf, "%d %d", worst, cnt);
    return buf;
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        int M, N;
        cin >> M >> N;
        vector<string> S(M);
        for (int j = 0; j < M; ++j) {
            cin >> S[j];
        }
        cout << "Case #" << i << ": " << result(N, S) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
