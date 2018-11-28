#include <bits/stdc++.h>
#include <omp.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

const int kMaxTestCase = 101;
const int kNumThread = 4;
inline int mgets(char in[]) { unsigned int c, n = 0; while ((c = gc())) { if (!~c and !n) exit(0); if (!~c or c == 10) break; in[n++] = c; } return in[n] = 0, n; }


template<class T> struct IndexGetter {
    map<T, int> fmp;
    vector<T> rmp;
    int n;
    IndexGetter() { n = 0; }
    int get(T a) {
        if (!fmp.count(a)) { fmp[a] = n, rmp.push_back(a); return n++; }
        return fmp[a];
    }
    T rget(int idx) { return rmp[idx]; }
    int size() { return n; }
    void clear() { n = 0, fmp.clear(), rmp.clear(); }
};

vector<string> split_string(string str, string delim = "") {
    vector<string> res;
    for (int i = 0; i < (int)str.size(); i++) if (delim.find(str[i]) != string::npos) str[i] = ' ';
    stringstream ss(str);
    while (ss >> str) res.push_back(str);
    return res;
}

char buf[1000000];

struct InputParameters {
    int n;
    vector<int> words[22];
    IndexGetter<string> name;
    void get() {
        n = getint();
        for (int i = 0; i < n; i++) {
            mgets(buf);
            vector<string> vstr = split_string(buf);
            words[i].clear();
            for (int j = 0; j < (int)vstr.size(); j++) {
                int w = name.get(vstr[j]);
                words[i].push_back(w);
            }
            sort(words[i].begin(), words[i].end());
            words[i].erase(unique(words[i].begin(), words[i].end()), words[i].end());
        }
    }
};

struct Result {
    int res;
    void print(int test_case) {
        printf("Case #%d: ", test_case + 1);
        printf("%d\n", res);
    }
};

InputParameters in[kMaxTestCase];
Result result[kMaxTestCase];

struct CaseSolver {
    void solve(InputParameters& in, Result& out, int test_case) {
        int i, j;
        int n =in.n;
        int res = 1 << 29;
        for (int h = 0; h < 1 << in.n; h++) {
            if (h & 1) continue;
            if ((h & 2) == 0) continue;
            vector<int> eng = in.words[0];
            vector<int> fre = in.words[1];
            for (i = 2; i < n; i++) {
                for (int j = 0; j < (int)in.words[i].size(); j++) {
                if (h >> i & 1) {
                    eng.push_back(in.words[i][j]);
                } else {
                    fre.push_back(in.words[i][j]);
                    }
                }
            }
            int cnt = 0;
            sort(eng.begin(), eng.end());
            eng.erase(unique(eng.begin(), eng.end()), eng.end());
            sort(fre.begin(), fre.end());
            fre.erase(unique(fre.begin(), fre.end()), fre.end());
            for (int i = 0; i < (int)eng.size(); i++) {
                if (binary_search(fre.begin(), fre.end(), eng[i])) {
                    cnt++;
                }
            }
            chmin(res, cnt);
        }
        out.res = res;
        fprintf(stderr, "-->%d done at %d.\n", test_case, omp_get_thread_num());
        return;
    }
};

CaseSolver solver[kNumThread];

int main () {
    int t, test_case = getint();
    omp_set_num_threads(kNumThread);
    for (t = 0; t < test_case; t++) { in[t].get(); }
#pragma omp parallel for schedule (dynamic, 1)
    for (t = 0; t < test_case; t++) { solver[omp_get_thread_num()].solve(in[t], result[t], t); }
    for (t = 0; t < test_case; t++) { result[t].print(t); }
    return 0;
}
