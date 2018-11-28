#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <utility>
#include <iomanip>

using namespace std;

typedef long long LL;
template<typename T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<typename T> inline T Sqr(const T& x) { return x * x; }

const LL MOD = 1000002013;

void Solution() {
    LL N, M;
    cin >> N >> M;
    map<int, vector<LL> > events;
    LL answer = 0;
    for (int i = 0; i < M; ++i) {
        LL from, to, how;
        cin >> from >> to >> how;
        events[from].push_back(how);
        events[to].push_back(-how);
        LL dist = to - from;
        answer = (answer + how * (N * dist - (dist * (dist - 1)) / 2)) % MOD;
    }    
    LL small = 0;
    //sort(events.begin(), events.end());
    map<LL, LL> cur;
    LL last = 0;
    for (map<int, vector<LL> >::iterator it = events.begin(); it != events.end(); ++it) {
        map<LL, LL> ncur;
        LL dist = it->first - last;
        for (map<LL, LL>::iterator jt = cur.begin(); jt != cur.end(); ++jt) {
            small = (small + jt->second * ((((dist)*(2*N - 2*jt->first - dist + 1))/2) % MOD)) % MOD;
            ncur[jt->first + dist] += jt->second;
        }
        last = it->first;
        vector<LL>& v = it->second;
        sort(v.rbegin(), v.rend());
        for (int i = 0; i < v.size(); ++i) {
            if (v[i] >= 0) {
                ncur[0] += v[i];
            } else {
                v[i] *= -1;
                while (v[i] > 0) {
                    if (v[i] < ncur.begin()->second) {
                        ncur.begin()->second -= v[i];
                        v[i] = 0;
                    } else {
                        v[i] -= ncur.begin()->second;
                        ncur.erase(ncur.begin());
                    }
                }
            }
        }
        cur.swap(ncur);
    }
    cout << (answer - small + MOD) % MOD << endl;
}


struct Timer {
    map<string, float> starts;
    void Tic(const string& name) { starts[name] = clock(); }
    float Toc(const string& name) { return (clock() - starts[name]) / CLOCKS_PER_SEC; }
} timer;

int main(int argc, char* argv[]) {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    ios_base::sync_with_stdio(false);

    timer.Tic("global");
    int testsNumber;
    cin >> testsNumber;
    for (int curTest = 1; curTest <= testsNumber; ++curTest) {
        cout << "Case #" << curTest << ": ";
        cerr << "Case #" << setw(2) << setfill('0') << curTest << ": running...";
        timer.Tic("test");
        Solution();
        cerr << "done! Elapsed time is " << setprecision(3) << timer.Toc("test") << endl;
    }
    cerr << endl << "Total elapsed time is " << setprecision(3) << timer.Toc("global") << endl;

    return 0;
}
