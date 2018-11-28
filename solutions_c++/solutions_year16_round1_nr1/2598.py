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
        string a, b;
        cin >> a;
        for(auto c : a) {
            if(!b.size()) {
                b += c;
            } else {
                if(c < b[0]) b = b + c;
                else b = c + b;
            }
        }
        cout << b << endl;
    }

    return 0;    
}
