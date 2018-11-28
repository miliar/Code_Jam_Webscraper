#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;

#define ll long long

map<string, int> cache;
int gv(const string& s) {
    if(cache.count(s) == 1) return cache[s];
    int n = cache.size();
    cache[s] = n;
    return n;
}

vector<int> split(const string& s) {
    string cur;
    vector<int> ret;
    for (int i=0;i<s.size();++i) {
        if (s[i] == ' ') {
           ret.push_back(gv(cur));
           cur="";
        } else cur += s[i];
    }
    ret.push_back(gv(cur));
    return ret;
}

int main() {
    int T;
    cin>>T;

    for (int t=1;t<=T;++t) {
        cache.clear();
        int N;

        cin>>N;
        string s;
        getline(cin, s);
        string A;
        string B;
        vector<vector<int>> S;
        for (int i=0;i<N;++i) {
            getline(cin, s);
            S.push_back(split(s)); 
        }

        int ans = 1<<28;
        bool any = false;
        int NN = cache.size();
        bool EW[2000];
        bool FW[2000];
        for (int i=0;i<(1<<(N-2));++i) {
            memset(EW,0,sizeof(EW));
            memset(FW,0,sizeof(FW));

            for (int e : S[0]) {
                EW[e] = true;
            }
            for (int f : S[1]) {
                FW[f] = true;
            }

            for (int j=2;j<S.size();++j) {
                bool e = (i & (1<<(j-2)));
                bool *C = e ? EW : FW;

                for (int k=0;k<S[j].size();++k) {
                    C[S[j][k]] = true;
                }
            }
            int cur = 0;
            for (int i=0;i<NN;++i) {
                if (EW[i] && FW[i]) {
                    cur++;
                }
            }
            ans = std::min(cur, ans);

            /*
            set<int> E(S[0].begin(), S[0].end());
            set<int> F(S[1].begin(), S[1].end());
            for (int j=2;j<S.size();++j) {
                bool e = (i & (1<<(j-2)));
                set<int> &C = e ? E : F;
                C.insert(S[j].begin(), S[j].end());

            }
            set<int> R;
            set_intersection(E.begin(), E.end(), F.begin(), F.end(), inserter(R, R.begin()));

            ans = std::min(ans, R.size());
            */
        }

        printf("Case #%d: %d\n", t, ans);
    }
}
