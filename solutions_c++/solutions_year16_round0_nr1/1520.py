#include <iostream>
using namespace std;

int main() {

    bool volt[10];
    int t, n;

    cin >> t;

    for (int test=0; test<t; test++) {
        cin >> n;
        int x;
        if (n>0) {
            for (auto &b : volt)
                b = false;
            int db=0;
            for (int i=1; db<10; i++) {
                int num = i * n;
                while (num != 0) {
                    volt [num%10] = true;
                    num/=10;
                }

                db=0;
                for (auto j : volt)
                    db += j;
                x = n * i;
            }
        }

        cout << "Case #" << test+1 << ": ";
        if (n == 0)
            cout << "INSOMNIA" << endl;
        else cout << x << endl;
    }

    /*for (int n=1; n < 1000000; n++) {
        for (auto &b : volt)
            b = false;
        int db=0;
        for (int i=1; db<10; i++) {
            int num = i * n;
            while (num != 0) {
                volt [num%10] = true;
                num/=10;
            }

            db=0;
            for (auto j : volt)
                db += j;
            t[n] = n * i;
        }
        cout << "n: " << n << '\t' << t[n] << endl;
    }*/
    return 0;
}

