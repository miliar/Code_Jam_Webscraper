#include <bits/stdtr1c++.h>
using namespace std;

int main() {
    int t; cin >> t;
    int ca = 1;
    while (t--) {
        int k, c; cin >> k >> c;
        int s; cin >> s;
        cout << "Case #" << ca++ << ": ";
        for (int i=1; i<=k; i++)
            cout << i << " ";
        cout << endl;
    } 
}
