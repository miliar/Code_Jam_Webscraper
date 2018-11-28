/*
    https://code.google.com/codejam/contest/2974486/dashboard#s=p0
*/
#include <iostream>
#include <cstdio>

using namespace std;

int c[4] = {0, };

int main()
{
    int T, r, tmp;
    int num = 0;
    
    cin >> T;
     
    while (T--) {
        int d = 0;
        int res = -1;
        
        cin >> r;
        for (int i = 0; i < 4; i++) { // row
            for (int j = 0; j < 4; j++) { // col
                if (i == r - 1) 
                    cin >> c[j];
                else
                    cin >> tmp;
            }
        }
        
        cin >> r;
        for (int i = 0; i < 4; i++) { // row
            for (int j = 0; j < 4; j++) { // col
                cin >> tmp;
                if (i == r - 1) {
                    for (int k = 0; k < 4; k++) {
                        if (c[k] == tmp) {
                            res = tmp;
                            d++;
                        }
                    }
                }
            }
        }
        
        cout << "Case #" << (++num) << ": ";
        switch (d) {
            case 0:
                cout << "Volunteer cheated!" << endl;
                break;
            case 1:
                cout << res << endl;
                break;
            default:
                cout << "Bad magician!" << endl;
                break;        
        }
    }
    
    return 0;
}
