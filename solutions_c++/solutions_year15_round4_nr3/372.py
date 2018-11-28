#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin >> t;
    cin.get();
    for (int kase=1; kase<=t; kase++) {
        cout << "Case #" << kase << ": ";
        int N; cin >> N;
        N -= 2;
        cin.get();
        map<string, int> word;
        vector<bool> a(5000), b(5000);
        string s;
        getline(cin, s);
        string w;
        stringstream ss;
        ss << s;
        while (ss >> w) {
            if (!word.count(w))
                word[w] = word.size();
            a[word[w]] = 1;
        }
        getline(cin, s);
        ss.clear();
        ss << s;
        while (ss >> w) {
            if (!word.count(w))
                word[w] = word.size();
            b[word[w]] = 1;
        }

        vector<vector<int> > S(N);
        for (int i=0; i<N; i++) {
            getline(cin, s);
            ss.clear();
            ss << s;
            while (ss >> w) {
                if (!word.count(w))
                    word[w] = word.size();
                S[i].push_back(word[w]);
            }
        }

        int ans = 10000000;
        vector<bool> c(5000), d(5000);
        for (int mask=0; mask<(1 << N); mask++) {
            c = a;
            d = b;
            for (int i=0; i<N; i++) {
                for (int j=0; j<S[i].size(); j++)
                    if (mask & (1 << i))
                        c[S[i][j]] = 1;
                    else
                        d[S[i][j]] = 1;
            }
            int cur = 0;
            for (int i=0; i<5000; i++) {
                cur += (c[i] && d[i]);
            }
            ans = min(ans, cur);
        }
        cout << ans << '\n';
    }
    return 0;
}
