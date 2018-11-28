#include <iostream>
#include <memory.h>

using namespace std;

const int n = 4;

int ca, cb;
int a[4][4], b[4][4];
int dx[17];

int res;


void input() {
    int i, j;

    cin >> ca; ca--;
    for (i=0; i<n; i++) for (j=0; j<n; j++) cin >> a[i][j];

    cin >> cb; cb--;
    for (i=0; i<n; i++) for (j=0; j<n; j++) cin >> b[i][j];
}


void solve() {
    int i, cnt = 0;
    memset(dx, 0, sizeof(dx)); 
    
    for (i=0; i<n; i++) ++dx[ a[ca][i] ];
    for (i=0; i<n; i++) ++dx[ b[cb][i] ];

    res = -1;  // cheated
    for (i=1; i<=16; i++) if (dx[i]==2) {
        cnt++;
        res = i;
    }
    
    if (cnt>1) res = -2; // bad magician
}

int main() {
    int i, num_test;

    cin >> num_test;
    for (i=1; i<=num_test; i++) {
        input();
        solve();
        
        cout << "Case #" << i << ": ";
        if (res == -1) cout << "Volunteer cheated!";
        else if (res == -2) cout << "Bad magician!";
        else cout << res;
        cout << endl;
    }
    return 0;
}
