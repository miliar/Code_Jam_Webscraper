#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RANGE(i,b,e) for(int (i)=(b);(i)<(int)(e);(i)++)
#define CRANGE(i,b,e) for(int (i)=(b);(i)<=(int)(e);(i)++)
#define RRANGE(i,b,e) for(int (i)=(b);(i)>=(int)(e);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433832795
#define INF 0x7FFFFFFF

int T;
vector<string> ori, sim;
vector<vector<int> > rep;

string simplify(string s)
{
    string s2;
    REP(i, s.size()) {
        if (i == 0 || s[i] != s[i - 1]) {
            string stemp(1, s[i]);
            s2.append(stemp);
        }
    }
    return s2;
}

vector<int> repeat(string s)
{
    vector<int> v;
    int cnt = 0;
    REP(i, s.size()) {
        if (i == 0) {
            cnt = 1;
        } else if (s[i] != s[i - 1]) {
            v.push_back(cnt);
            cnt = 1;
        } else {
            cnt++;
        }
    }
    v.push_back(cnt);
    return v;
}

int count(const vector<vector<int> > &rep, int j)
{
    vector<int> col;
    REP(i, rep.size()) {
        col.push_back(rep[i][j]);
    }

    int sum = 0;
    for (int val : col) {
        sum += val;
    }
    sum /= col.size();

    int res1 = 0, res2 = 0;
    REP(i, col.size()) {
        res1 += abs(col[i] - sum);
        res2 += abs(col[i] - (sum + 1));
    }
    return min(res1, res2);
}

int main(int argc, char **argv)
{
    cin >> T;
    for (int t = 0;t < T;t++) {
        ori.clear();
        sim.clear();
        rep.clear();

        int N;
        cin >> N;
        REP(i, N) {
            string s;
            cin >> s;
            ori.push_back(s);
            sim.push_back(simplify(s));
            rep.push_back(repeat(s));
        }

        bool ok = true;
        REP(i, N) {
            if (sim[i] != sim[0]) {
                ok = false;
                break;
            }
        }

        //  Output.
        cout << "Case #" << t + 1 << ": ";
        if (!ok) {
            cout << "Fegla Won" << endl;
            continue;
        }

        int cnt = 0;
        REP(j, rep[0].size()) {
            cnt += count(rep, j);
        }

        cout << cnt << endl;
    }

    return 0;
}
