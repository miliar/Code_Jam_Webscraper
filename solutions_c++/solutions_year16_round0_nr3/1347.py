#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int x[32];

int volt[500][32];

int main() {

    srand(time(NULL));
    int t, n, j;
    int db=0;
    cin >> t >> n >> j;
    cout << "Case #1:\n";
    x[0] = x[1] = x[n-2] = x[n-1] = 1;
    while (db < j) {
        int sum=0;
        for (int i=2; i<n-3; i+=2) {
            x[i] = rand() % 2;
            x[i+1]=x[i];
        }
        for (int i=0; i<n; i++)
            sum += x[i];
        if (sum % 6 == 0) {

            bool jo = true;
            for (int i=0; i<db && jo; i++) {
                bool egyez = true;
                for (int j=0; j<n && egyez; j++)
                    if (x[j] != volt[i][j])
                        egyez = false;
                if (egyez)
                    jo = false;
            }
            if (jo) {
                for (int i=0; i<n; i++) {
                    volt[db][i] = x[i];
                    cout << x[i];
                }
                cout << " 3 2 3 2 7 2 3 2 3\n";
                db++;
            }
        }
    }
}
