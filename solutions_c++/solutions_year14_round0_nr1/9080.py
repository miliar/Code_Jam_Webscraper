#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int i, j;
    int T, NT;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cout<<"Case #"<<T<<": ";
        set<int> s;
        int r;
        int n[16];
        cin>>r;
        --r;
        for(i=0; i<16; ++i) cin>>n[i];
        for(i=r*4; i<(r+1)*4; ++i) {
            s.insert(n[i]);
        }
        cin>>r;
        --r;
        for(i=0; i<16; ++i) cin>>n[i];
        for(i=0; i<r*4; ++i) s.erase(n[i]);
        for(i=(r+1)*4; i<16; ++i) s.erase(n[i]);
        if (s.size() == 0) {
            cout<<"Volunteer cheated!";
        } else if (s.size() > 1) {
            cout<<"Bad magician!";
        } else {
            cout<<*(s.begin());
        }
        cout<<"\n";
    }

    return 0;
}
