#include <fstream>
#include <cmath>

using namespace std;

ifstream cin("a.in");
ofstream cout("a.out");

const int NMAX = 1007;

int T, n, a[NMAX];

int main() {
    cin >> T;
    int x = 0;
    while(T--) {
        cin >> n;
        ++x;
        for(int i = 1; i <= n; ++i) {
            cin >> a[i];
        }
        cout << "Case #" << x << ": ";
        int N = n, poz, poz2;
        while(N > 0) {
            int sum = 0, Max = 0, Maxx;
            for(int i = 1; i <= n; ++i) {
                sum += a[i];
            }
            sum /= n;
            for(int i = 1; i <= n; ++i) {
                if(fabs(sum - a[i]) >= Max) {
                    if(fabs(sum - a[i]) == Max) {
                        if(Maxx < a[i]) {
                            poz = i;
                            Maxx = a[i];
                        }
                    }
                    else {
                        poz = i;
                        Max = fabs(sum - a[i]);
                        Maxx = a[i];
                        }
                }
            }
            N = 0;
            for(int i = 1; i <= n; ++i) {
                if(a[i] != 0) {
                    ++N;
                }
            }
            if(N > 2) {
                cout << (char) (poz + 'A' - 1) << " ";
                --a[poz];
            }
            else {
                if(N == 2) {
                    poz = 0;
                    for(int i = 1; i <= n; ++i) {
                        if(a[i] != 0) {
                            if (poz != 0) {
                                poz2 = i;
                            }
                            else {
                                poz = i;
                            }
                        }
                    }
                    --a[poz];
                    --a[poz2];
                    cout << (char) (poz + 'A' - 1) << (char) (poz2 + 'A' - 1) << " ";
                }
            }
        }
        cout << "\n";
    }
    return 0;
}
