#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    vector<int> res;
    vector<int> a[4];
    vector<int> b[4];
    cin >> t;
    for(int i=1;i<=t;i++) {
        res.clear();
        for(int j=0;j<4;j++) {
            a[j].clear();
            b[j].clear();
        }
        int n,m,v;
        cin >> n; n --;
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                cin >> v;
                a[j].push_back(v);
            }
        }
        cin >> m; m --;
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                cin >> v;
                b[j].push_back(v);
            }
        }
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                if(a[n][j] == b[m][k]) {
                    res.push_back(a[n][j]);
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(res.size() == 0) cout << "Volunteer cheated!" << endl;
        else if(res.size() > 1) cout << "Bad magician!" << endl;
        else cout << res[0] << endl;
    }
    return 0;
}
