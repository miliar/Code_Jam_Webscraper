#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
using namespace::std;

// Bipartite matching algorithm is copied from:
// https://web.stanford.edu/~liszt90/acm/notebook.html#file5
typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] && !seen[j]) {
            seen[j] = true;
            if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
    mr = VI(w.size(), -1);
    mc = VI(w[0].size(), -1);

    int ct = 0;
    for (int i = 0; i < w.size(); i++) {
        VI seen(w[0].size());
        if (FindMatch(i, w, mr, mc, seen)) ct++;
    }
    return ct;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        int N;
        cin >> N;

        set<string> left;
        set<string> right;
        set<pair<string, string> > s;
        for (int i = 0; i < N; ++i)
        {
            string l, r;
            cin >> l;
            cin >> r;

            left.insert(l);
            right.insert(r);

            s.insert(make_pair(l, r));
        }

        int m = left.size();
        int n = right.size();
        VVI w(m, VI(n, 0));
        int i = 0;
        int j = 0;
        for (set<string>::iterator it1 = left.begin(); it1 != left.end(); ++it1)
        {
            for (set<string>::iterator it2 = right.begin(); it2 != right.end(); ++it2)
            {
                set<pair<string, string> >::iterator it = s.find(pair<string, string> (*it1, *it2));
                if (it != s.end())
                {
                    w[i][j] = 1;
                }

                ++j;
            }
            j = 0;
            ++i;
        }


        VI mr;
        VI mc;

        int k = BipartiteMatching(w, mr, mc);
        int ans = N - (k + (m - k) + (n - k));

        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
}
