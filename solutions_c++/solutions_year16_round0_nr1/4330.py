using namespace std;

#include <cstdio>
#include <iostream>
#include <list>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <typeinfo>

int digits[10];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T, n;
    cin >> T;
    
    for (int t = 0; t < T; t++) {
        for (int j = 0; j < 10; j++)
            digits[j] = 0;
        cin >> n;
        bool fl;
        cout << "Case #" << t + 1 << ": ";
        if (n == 0)
            cout << "INSOMNIA";
        else {
            for (int i = 1; i < 1000; i++) {
                int m = n * i;
                
                int q = m;
                while (q > 0) {
                    digits[q % 10] = 1;
                    q /= 10;
                }
                
                fl = true;
                for (int j = 0; j < 10; j++)
                    if (digits[j] == 0)
                        fl = false;
                if (fl) {
                    cout << n * i;
                    break;
                }
            }
            if (fl == 0)
                cout << "INSOMNIA";
        }
        cout << endl;
    }
    return 0;
}
