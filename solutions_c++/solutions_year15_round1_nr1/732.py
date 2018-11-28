#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ifstream cin("stuff.in");
    ofstream cout("stuff.out");
    
    int t; cin >> t; int mush[1005];
    for (int i = 0; i < t; ++i) {
        int n; cin >> n; for (int j = 0; j < n; ++j)
            cin >> mush[j];
        int tot1 = 0, maxd = 0, tot2 = 0;
        for (int j = 0; j < n-1; ++j) {
            tot1 += max(0, mush[j]-mush[j+1]);
            maxd = max(maxd, mush[j]-mush[j+1]);
        }
        
        for (int j = 0; j < n-1; ++j)
            tot2 += min(maxd, mush[j]);
        
        cout << "Case #" << i+1 << ": " << tot1 << ' ' << tot2 << endl;
    }
}