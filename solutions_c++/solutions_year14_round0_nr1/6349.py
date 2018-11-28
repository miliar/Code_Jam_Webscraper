#include <iostream>

using namespace std;



int main() {
    int t;

    cin >> t;

    for(int i = 1; i<=t; i++) {
        int a1, a2;
        int r1[4];
        int r2[4];
        int t[4];
        cin >> a1;

        for(int j = 1; j<=4; j++) {
            if(j==a1) {
                cin >> r1[0] >> r1[1] >> r1[2] >> r1[3];
            } else {
                cin >> t[0] >> t[1] >> t[2] >> t[3];
            }
        }

        cin >> a2;

        for(int j = 1; j<=4; j++) {
            if(j==a2) {
                cin >> r2[0] >> r2[1] >> r2[2] >> r2[3];
            } else {
                cin >> t[0] >> t[1] >> t[2] >> t[3];
            }
        }

        int matches = 0;
        int answer = 0;

        for(int j=0; j<4; j++) {
            for(int k=0; k<4; k++) {
                if(r1[j]==r2[k]) {
                    matches++;
                    answer = r1[j];
                    //cout << "Hit: " << j << " x " << k << endl;
                }
            }
        }

        cout << "Case #" << i << ": ";
        if(matches==0) cout << "Volunteer cheated!" << endl;
        if(matches==1) cout << answer << endl;
        if(matches>1) cout << "Bad magician!" << endl;

    }
}

