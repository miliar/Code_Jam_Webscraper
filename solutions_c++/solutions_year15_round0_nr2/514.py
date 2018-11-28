#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream cin("testB.in");
    ofstream cout("testB.out");

    int t; cin >> t;

    for(int tCase = 1; tCase <= t; ++tCase) {
        cout << "Case #" << tCase << ": ";
        
        int n; cin >> n;
        multiset<int> A;
        for(int i = 0; i < n; ++i) {
            int a; cin >> a;
            A.insert(a);
        }
        int ans = 1e6;
        
        for(int maxx = 1; maxx <= 1000; ++maxx) {
            int steps = 0;
            multiset<int> S = A;
            while(*S.rbegin() > maxx) {
                steps++;
                if(steps > 1000)
                    break;
                int toSplit = *S.rbegin();
                S.erase(S.find(toSplit));
                S.insert(toSplit - maxx);
            }
            ans = min(ans, maxx + steps);
        }

        cout << ans << "\n";
    }
}
