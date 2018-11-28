#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

int ct = 0; int d, panc[1005];

int comp(int x) {
    set<pii> s; ct = d-1; for (int i = 0; i < d; ++i)
        s.insert(pii(panc[i], i));
    int tot = 0; while ((*s.rbegin()).first > x) {
        pii t = *s.rbegin(); s.erase(t);
        ++tot; ++ct; s.insert(pii(x, t.second));
        s.insert(pii(t.first-x, ct));
    }
    
    return tot;
}

int main() {
    ifstream cin("stuff.in");
    ofstream cout("stuff.out");
    
    int t; cin >> t; for (int i = 0; i < t; ++i) {
        cin >> d; for (int j = 0; j < d; ++j)
            cin >> panc[j];
        
        int mini = 1005; for (int i = 1; i <= 1005; ++i)
            mini = min(mini, i+comp(i));
        
        cout << "Case #" << i+1 << ": " << mini << endl;
    }
}
