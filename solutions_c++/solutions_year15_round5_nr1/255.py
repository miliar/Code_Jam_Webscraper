#include <cassert>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;


#define less dsjkfjdslkfjslf
#define more dsjkfjdslkfjslfdhfjd
#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(int i = 0;i < (n);++i)

long long MOD = 1000000007;
int T;

long long s[1000010];
long long m[1000010];
vector<int> v[1000000];
int used[1000010];
pair<int, int> forsort[1000010];
int less[1010];
int more[1010];
long long n, d;
int summ;
int curl;

void add(int start) {
    if (start && !used[m[start]])
        return;
    if (used[start])
        return;
    ++summ;
    //cerr << " add " << start << endl;
    used[start] = 1;
    FOR(i, v[start].size()) {
        int anc = v[start][i];
        if (s[anc] >= curl && s[anc] <= curl+d)
            add(anc);
    }
}

void del(int start) {
    if (!used[start])
        return;
    used[start] = 0;
    --summ;
    //cerr << " del " << start << endl;
    FOR(i, v[start].size()) {
        int anc = v[start][i];
        del(anc);
    }
}

int main() {
    cin >> T;
    FOR(itest, T) {
        cin >> n >> d;
        long long as,cs,rs, am, cm, rm;
        cin >> s[0] >> as >> cs >> rs;
        cin >> m[0] >> am >> cm >> rm;
        v[0].clear();
        for (int i = 1; i < n; ++i) {
            v[i].clear();
            s[i] = (s[i-1] * as + cs) % rs;
            m[i] = (m[i-1] * am + cm) % rm;
            //cerr << s[i] << endl;
        }
        for (int i = 1; i < n; ++i) {
            used[i] = 0;
            m[i] = m[i] % i;
            v[m[i]].push_back(i);
        }

        FOR(i, n) {
            forsort[i] = mp(s[i], i);
            used[i] = 0;
        }
        sort(forsort, forsort + n);

        int last1 = 0;
        int last2 = 0;
        summ = 0;
        int bestans = 0;
        for (int i = 0; i < 1000 + d; ++i) {
            //cerr << i << endl;
            while (last1 < n && i >= forsort[last1].first) {
                curl = i - d;
                add(forsort[last1].second);
                //cerr << "summ " << summ << endl;
                ++last1;
            }

            while (last2 < n && i - d > forsort[last2].first) {
                curl = i - d;
                del(forsort[last2].second);
                //cerr << "summ " << summ << endl;
                ++last2;
            }
            if (s[0] >= i-d && s[0] <= i) {
                //cerr << i << " " << summ << endl;
                // //cerr << i << " " << less[i-d] << " " << more[i] << " " << summ << " " << less[i-d] + more[i] - summ << endl;
                bestans = max(bestans, summ);
            }
        }

        cout << "Case #" << (itest + 1) << ": " << bestans << endl;
    }
}