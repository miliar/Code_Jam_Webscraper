#include <bits/stdc++.h>
using namespace std;

typedef long long li;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

const int bitsize = 64;
struct mbitset {
    int cap;

    vector<unsigned long long> data;
    mbitset(int n):cap(n), data(n / bitsize + 1) {
    }

    void add(unsigned long long p) {
        data[p / bitsize] |= 1ULL << p;
    }

    mbitset intersect(const mbitset& that) {
        mbitset ret(cap);
        rep(i, data.size()) {
            ret.data[i] = data[i] & that.data[i];
        }
        return ret;
    }

    int size() {
        int ans = 0;
        rep(i, data.size()) {
            ans += __builtin_popcountll(data[i]);
        }
        return ans;
    }
};

struct problem {
    // input fields.
    int n;
    map<string, int> v2i;
    vector<vector<int> > sents;
    int ans;

    // parse here.
    problem () {
        cin >> n;
        
        string line;
        getline(cin, line);
        rep(i, n) {
            getline(cin, line);
            sents.push_back(conv(line));
        }
    }

    vector<int> conv(const string line) {
        istringstream iss(line);
        string word;
        vector<int> ret;
        while (iss >> word) {
            if (v2i.find(word) == v2i.end()) {
                int nv = v2i.size();
                v2i[word] = nv;
            }
            ret.push_back(v2i[word]);
        }
        return ret;
    }

    // called exactly once. set ans here.
    void solve () {
        int vsize = v2i.size();
        mbitset eb(vsize), fb(vsize);
        rep(i, sents[0].size()) {
            eb.add(sents[0][i]);
        }
        rep(i, sents[1].size()) {
            fb.add(sents[1][i]);
        }
                
        ans = 1e9;

        const int m = n - 2;
        const int pat = 1 << m;
        rep(mask, pat) {
            mbitset e (eb);
            mbitset f (fb);

            rep(p, m) {
                if ((mask >> p) & 1) {
                    rep(i, sents[p+2].size()) {
                        e.add(sents[p+2][i]);
                    }           
                } else {
                    rep(i, sents[p+2].size()) {
                        f.add(sents[p+2][i]);
                    }           
                }
            }
            ans = min(ans, (int)(e.size() + f.size() - v2i.size()));
        }
    }
};

// generally you don't have to modify below.
int main () {
    int t;
    cin >> t;
    vector<problem> inputs;
    rep (i, t) {
        inputs.push_back(problem());
    }
    //#pragma omp parallel for
    rep (i, t) {
        inputs[i].solve();
    }
    rep (i, t) {
        cout << "Case #" << i + 1 << ": " << inputs[i].ans << endl;
    }
    return 0;
}

