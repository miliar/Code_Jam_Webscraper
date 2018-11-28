#include <iostream>

using namespace std;

int main() {
    int cases,x,y,ans;
    bool a[20];
    cin >> cases;
    for (int caseno = 1; caseno <= cases; caseno++) {
        cout << "Case #" << caseno << ": ";
        for (int i = 1; i < 20; i++) {
            a[i] = false;
        }
        ans = 0;
        
        cin >> x;
        for (int i = 1; i <= 4; i++) {
            if (i!=x) {
                for (int j = 0; j < 4; j++) {
                    cin >> y;
                }
            } else {
                for (int j = 0; j < 4; j++) {
                    cin >> y;
                    a[y] = true;
                }
            }
        }
        
        cin >> x;
        for (int i = 1; i <= 4; i++) {
            if (i!=x) {
                for (int j = 0; j < 4; j++) {
                    cin >> y;
                }
            } else {
                for (int j = 0; j < 4; j++) {
                    cin >> y;
                    if (a[y]) {
                        if (ans == 0) {
                            ans = y;
                        } else {
                            ans = -1;
                        }
                    }
                }
            }
        }
        
        if (ans == -1) {
            cout << "Bad magician!" << endl;
        } else if (ans == 0) {
            cout << "Volunteer cheated!" << endl;
        } else {
            cout << ans << endl;
        }
    }
}