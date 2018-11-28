#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out.txt", "wt", stdout);

    int T;
    cin>>T;
    for (int cas=1; cas<=T; ++cas) {
        int n, x;
        cin>>n>>x;
        multiset<int> c;
        for (int i=0; i<n; ++i) {
            int C;
            cin>>C;
            c.insert(C);
        }
        int cnt = 0;
        while (c.size()) {
            ++cnt;
            int t = x;
            set<int>::iterator it = c.end();
            --it;
            t -= *it;
            c.erase(it);
            if (c.size()) {
                it = c.upper_bound(t);
                if (it != c.begin()) {
                    --it;
                    c.erase(it);
                }
            }
        }
        cout<<"Case #"<<cas<<": "<<cnt<<endl;
    }

    return 0;
}
