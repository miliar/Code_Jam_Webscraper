#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 1000;

int A[MAXN];

int main() {
    int cases; cin >> cases;
    for (int tc = 1; tc <= cases; tc++) {
        cout << "Case #" << tc << ": " ;
        int N, X, a;
        cin >> N >> X;
        fill (A, A + MAXN, 0);
        for (int i = 0; i < N; i++) { 
            cin >> a;
            A[a] ++;
        }
        int ret = 0, g = 0;
        for (int i = X; i >= 0; i--) {
            if (A[i] > 0) {
                if (i + i < X){
                    g += A[i];
                }
                else if (i + i == X) {
                    ret += (A[i] + 1) / 2;
                } else {
                    ret += A[i];
                    int t = X - i;
                    while (t > 0 && A[i] > 0) {
                        if (A[t] > 0) {
                            int m =  min(A[t], A[i]);
                            A[t] -= m;
                            A[i] -= m;
                         }
                        t --;
                    }
                }
            }
        }
        ret += (g + 1) / 2;

        cout << ret << endl;
    } 
}
