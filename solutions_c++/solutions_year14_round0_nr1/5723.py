#include <iostream>

using std::cout;
using std::endl;
using std::cin;

int main(){
    int T;
    cin >> T;

    bool b[17];
    int ans;
    int n;

    for (int i = 1; i <= T; ++i) {
        for (int j = 0; j < 17; ++j)
            b[j] = 0;
        ans = 0;
        n = 0;
        int row;
        cin >> row;
        for (int j = 1; j <= 4; ++j)
            for (int k = 1; k <= 4; ++k) {
                int tmp;
                cin >> tmp;
                if (j == row)
                    b[tmp] = 1;
            }
        cin >> row;
        for (int j = 1; j <= 4; ++j)
            for (int k = 1; k <= 4; ++k) {
                int tmp;
                cin >> tmp;
                if (j != row)
                    b[tmp] = 0;
            }
        for (int j = 1; j <= 16; ++j)
            if (b[j]) {
                ans = j;
                ++n;
            }
        cout << "Case #" << i << ": ";
        switch(n) {
            case 0:
                cout << "Volunteer cheated!" << endl;
                break;
            case 1:
                cout << ans << endl;
                break;
            default:
                cout << "Bad magician!" << endl;
        }
  }
  return 0;
}
