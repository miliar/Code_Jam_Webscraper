#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)

int main(){
    int T;
    cin >> T;
    rep(n, T) {
        int possible[17];
        rep(i,17) possible[i] = 0;
        rep(i, 2) { 
            int row, card[4][4];
            cin >> row;
            row--;
            rep(y,4) {
                rep(x, 4) {
                    cin >> card[x][y];
                }
            }
            rep(x, 4) {
                possible[card[x][row]] ++;
            }
        }
        int cnt = 0;
        for(int i=1; i<=16; i++) {
            if( possible[i] == 2 ) {
                cnt++;
            }
        }
        cout << "Case #" << (n+1) << ": ";
        if( cnt == 0 ) {
            cout << "Volunteer cheated!" << endl;
        } else if( cnt == 1 ) {
            for(int i=1; i<=16; i++) {
                if( possible[i] == 2 ) {
                    cout << i << endl;
                    break;
                }
            }
        } else {
            cout << "Bad magician!" << endl;
        }
    }
    return 0;
}

