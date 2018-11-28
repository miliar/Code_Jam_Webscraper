#include <iostream>
using namespace std;

int main() {
    int t; cin>>t;
    for(int ti=1;ti<=t;++ti) {
        int c[4][4][2] = {};
        int a[2] = {};
        int d[17][2] = {};
        for(int k=0;k<2;++k) {
            cin>>a[k];
            a[k]--;
            for(int i=0;i<4;++i) {
                for(int j=0;j<4;++j) {
                    cin>>c[i][j][k];
                    d[c[i][j][k]][k] = i;
                }
            }
        }
            
            bool bad = false;
            int ans[4] = {};
            for(int i=0;i<4;++i) {
                int num = c[a[0]][i][0];
                int ri = d[num][1]; 
                //cerr << num << ' ' << ri << endl;
                if(ans[ri] != 0) {
                    bad = true;
                    ans[ri] = -1;
                } else {
                    ans[ri] = num;
                    //cerr << num << ' ' << ans[ri] << endl;
                }
            }
            //for(int i=0;i<4;++i) cerr << ans[i] << ' '; cerr << endl;
            cout << "Case #" << ti << ": ";
            if(ans[a[1]] == 0) {
                cout << "Volunteer cheated!" << endl;
            }else if(ans[a[1]] < 0) {
                cout << "Bad magician!" << endl;
            }else {
                cout << ans[a[1]] << endl;
            }
    }
    return 0;
}
