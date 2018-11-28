#include <iostream>
using namespace std;
int l[4][4];
int p(int x, int y) {
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;

    for (int i = 0; i < 4; ++i) {
        if (x == 0) {
            if (l[x+i][y] == 'X') ++a;
            else if (l[x+i][y] == 'O') --a;
            else if (l[x+i][y] == 'T') a = a;
            else a = 9999;
        }
        if (y == 0) {
            if (l[x][y+i] == 'X') ++b;
            else if (l[x][y+i] == 'O') --b;
            else if (l[x][y+i] == 'T') b = b;
            else b = 9999;
        }
        if (x == 0 && y == 0) {
            if (l[x+i][y+i] == 'X') ++c;
            else if (l[x+i][y+i] == 'O') --c;
            else if (l[x+i][y+i] == 'T') c = c; 
            else c = 9999;
        }
        if (x == 0 && y == 3) {
            if (l[x+i][y-i] == 'X') ++d;
            else if (l[x+i][y-i] == 'O') --d;
            else if (l[x+i][y-i] == 'T') d = d;
            else d = 9999;
        }
    }
    if (a >= 3 && a < 10) return 1;
    if (b >= 3 && b < 10) return 1;
    if (c >= 3 && c < 10) return 1;
    if (d >= 3 && d < 10) return 1;
    if (a <= -3 || b <= -3 || c <= -3 || d <= -3) { 
        return -1;
    }
    return 0;
}
int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int taynna = 1;
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                char tmp;
                cin >> tmp;
                l[j][k] = tmp;
                if (tmp == '.') taynna = 0;
            }
        }
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                int tmp = p(j, k);
                if (tmp == -1) {
                    cout << "Case #" << i+1 << ": O won\n";
                    goto ohi;
                }
                if (tmp == 1) {
                    cout << "Case #" << i+1 << ": X won\n";
                    goto ohi;
                }
            }
        }
        if (!taynna) {
            cout << "Case #" << i+1 << ": Game has not completed\n";
        }
        else {
            cout << "Case #" << i+1 << ": Draw\n";
        }
        ohi:; 
        
    }

}
