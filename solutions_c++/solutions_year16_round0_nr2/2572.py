#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

typedef int jnt;
#define int long long

#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define DEB(x) cerr << x << '\n';
#define endl '\n'

using namespace std;

jnt main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        string p;
        cin >> p;
        int side = p[0], count = 0;
        for(int i = 1; i < p.size(); ++i) {
            if(side != p[i] && ++count) side = p[i];
        }
        if(p.back() == '-') ++count;
        cout << "Case #" << i << ": " << count << endl;
    }
    return 0;
}
