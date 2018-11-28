#include <iostream>

using namespace std;

int main() {
    int m1[4][4], m2[4][4];
    int i, j, k, x, r1, r2, cnt, ans;
    int T;

    cin>>T;
    for (i=1; i<=T; ++i) {

        cin>>r1;
        for (j=0; j<4; ++j) {
            for(k=0; k<4; ++k) {
                cin>>m1[j][k];
            }
        }

        cin>>r2;
        for (j=0; j<4; ++j) {
            for(k=0; k<4; ++k) {
                cin>>m2[j][k];
            }
        }

        cnt=0;
        ans=0;
        for (j=0; j<4; ++j) {

            x = m1[r1-1][j];
            for (k=0; k<4; ++k) {
                if (x == m2[r2-1][k]) {
                    ++cnt;
                    ans=x;
                }
            }
        }

        cout<<"Case #"<<i<<": ";

        if (cnt > 1) {
            cout<<"Bad magician!\n";
        }
        else if (cnt == 1) {
            cout<<ans<<"\n";
        } 
        else {
            cout<<"Volunteer cheated!\n";
        }
    }

    return 0;
}


