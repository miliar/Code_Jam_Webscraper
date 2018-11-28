#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>
#include <set>
#include <cmath>
#include <iterator>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

vector<string> split(const string& s, const string& delim = " ") {
    vector<string> res;
    string t;
    for (int i = 0; i != s.size(); i++) {
        if (delim.find(s[i]) != string::npos) {
            if (!t.empty()) {
                res.push_back(t);
                t = "";
            }
        }
        else {
            t += s[i];
        }
    }
    if (!t.empty()) {
        res.push_back(t);
    }
    sort(res.begin(), res.end());
    res.erase(unique(res.begin(), res.end()), res.end());
    return res;
}

vector<int> status(3000);
int idx;

void run() {
    int N, res = -1;
    cin >> N;
    string english, french;
    getline(cin, english);
    getline(cin, english);
    getline(cin, french);
    N -= 2;
    vector<string> englishWords = split(english);
    vector<string> frenchWords = split(french);
    vector<int> eng, fr;
    idx = 0;
    map<string, int> mmp;
    REP(i, englishWords.size()) {
        string ss = englishWords[i];
        if (mmp.find(ss) == mmp.end()) mmp[ss] = idx++;
        eng.push_back(mmp[ss]);
    }
    REP(i, frenchWords.size()) {
        string ss = frenchWords[i];
        if (mmp.find(ss) == mmp.end()) mmp[ss] = idx++;
        fr.push_back(mmp[ss]);
    }
    vector<vector<int> > mm(N);
    REP(i, N) {
        string word;
        getline(cin, word);
        vector<string> ts = split(word);
        REP(j, ts.size()) {
            string ss = ts[j];
            if (mmp.find(ss) == mmp.end()) mmp[ss] = idx++;
            mm[i].push_back(mmp[ss]);
        }
    }

    status.assign(3000, -1);
    int sum = 0;

    REP(i, eng.size()) status[eng[i]] = 0;
    REP(i, fr.size()) {
        int cur = fr[i];
        if (status[cur] == -1) status[cur] = 1;
        else if (status[cur] == 0) {
            status[cur] = 2;
            ++sum;
        }
    }

    vector<int> cp = status;

    REP(st, (1 << N)) {
        status = cp;
        int t = sum;
        REP(i, N) {
            if (st & (1 << i)) {
                REP(j, mm[i].size()) {
                    int s = mm[i][j];
                    if (status[s] == -1) status[s] = 0;
                    else {
                        if (status[s] == 1) {
                            status[s] = 2;
                            ++t;
                        }
                    }
                }
            }
            else {
                REP(j, mm[i].size()) {
                    int s = mm[i][j];
                    if (status[s] == -1) status[s] = 1;
                    else {
                        if (status[s] == 0) {
                            status[s] = 2;
                            ++t;
                        }
                    }
                }
            }
            if (res != -1 && t >= res) break;
        }
        if (res == -1 || t < res) res = t;
    }
    cout << res << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c, 1, k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
