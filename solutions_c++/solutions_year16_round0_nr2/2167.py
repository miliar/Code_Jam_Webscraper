#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef complex<ld> pt;
typedef vector<pt> pol;
typedef vector<int> vi;
typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    for(int kase=1; kase<=N; kase++) {
        cout << "Case #" << kase << ": ";
        string zxcv;
        cin >> zxcv;
        char lastc = '=';
        int qwer = -1;
        for(auto c : zxcv) {
            if(c != lastc) qwer++;
            lastc = c;
        }
        if(lastc == '-') qwer++;
        cout << qwer << endl;
    }

    return 0;    
}
