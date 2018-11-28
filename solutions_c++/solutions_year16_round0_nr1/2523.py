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
    int t,k,c;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cin >> k;
        if((c=k) == 0) cout << "Case #" << i << ": INSOMNIA" << endl;
        else for(vector<int> done(10,0);;k += c) {
            string str = to_string(k);
            for(char a : str) if(!done[a-48]) {
                done[a-48] = 1; int totCount = 0;
                for(auto q : done) totCount += q;
                if(totCount == done.size()) {
                    cout << "Case #" << i << ": " << k << endl;
                    goto next;
                }
            }
        }
    next:;
    }
    return 0;
}
