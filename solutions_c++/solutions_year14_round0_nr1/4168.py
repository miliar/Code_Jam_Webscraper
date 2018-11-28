#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, p = 1;
    cin >> n;
    while(p <= n) {
    int i, j, k, l, m = 0, num;
    int a[4][4], b[4][4];

    cin >> i;
    for(k = 0; k < 4; k++) {
        for(l = 0; l < 4; l++) {
            cin >> a[k][l];
        }
    }

    cin >> j;
    for(k = 0; k < 4; k++) {
        for(l = 0; l < 4; l++) {
            cin >> b[k][l];
        }
    }
    i--;j--;
    for(k = 0; k < 4; k++) {
        for(l = 0; l < 4; l++) {
            if(a[i][k] == b[j][l]) {
                m++;
                num = a[i][k];
            }
        }
    }

    if(m == 1) {
        cout << "Case #"<< p << ": " << num << endl;;
    }
    else if(m >= 2) {
        cout << "Case #"<< p << ": Bad magician!" << endl;
    }
    else if (m == 0){
        cout << "Case #"<< p << ": Volunteer cheated!" << endl;
    }
    p++;
    }
    return 0;
}
