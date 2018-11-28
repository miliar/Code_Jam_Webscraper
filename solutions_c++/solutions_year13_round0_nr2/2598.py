#include <iostream>
using namespace std;
int n, m;
int a[111][111];

void run() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) cin >> a[i][j];
    int flag = 1;
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < m; j++) {
            int b1 = 1, b2 = 1;
            for(int k = 0; k < n; k++) if(a[i][j] < a[k][j]) b1 = 0;
            for(int k = 0; k < m; k++) if(a[i][j] < a[i][k]) b2 = 0;
            if(!b1 && !b2) flag = 0;
        }
    if(flag) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int t;
    cin >> t;
    for(int i = 1 ; i <= t; i++) {
        printf("Case #%d: ", i);
        run();
    }
    return 0;
}
