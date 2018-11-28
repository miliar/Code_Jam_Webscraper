#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    //freopen("A-small-attempt5.in","r",stdin);
    //freopen("A-small-attempt5.out", "w", stdout);
    int T, tn, r1, r2, i, j, tmp;
    cin>>T;
    vector<int> v1, v2, v3(10);
    for(tn = 1; tn <= T; ++tn) {
        cin>>r1;
        v1.clear(); v2.clear();
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                cin>>tmp;
                if (i == r1 - 1) {
                    v1.push_back(tmp);
                }
            }
        }
        cin>>r2;
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                cin>>tmp;
                if (i == r2 - 1) {
                    v2.push_back(tmp);
                }
            }
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        vector<int>::iterator it = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), v3.begin());
        v3.resize(it - v3.begin());
        cout<<"Case #"<<tn<<": ";
        if (v3.empty()) {
            cout<<"Volunteer cheated!"<<endl;
        } else if (v3.size() == 1) {
            cout<<v3[0]<<endl;
        } else {
            cout<<"Bad magician!"<<endl;
        }
        v3.resize(10);
    }
    return 0;
}
