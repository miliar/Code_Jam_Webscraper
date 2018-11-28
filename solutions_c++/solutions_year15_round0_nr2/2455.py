#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    fstream cin, cout;
    cin.open("input.txt", ios_base::in);
    cout.open("output.txt", ios_base::out);
    
    int t, ti;
    int d, a[10000], res, max, minute;
    int i, j;
    
    cin >> t;
    for (ti = 1; ti <= t; ++ti) {
        res = 0;
        cin >> d;
        for (i = 0; i < d; ++i) {
            cin >> a[i];
            max = (max > a[i]) ? max : a[i];
        }
        
        for (j = 1; j <= max; ++j) { //each max piece - j
            minute = 0;
            for (i = 0; i < d; ++i) { //divide to j
                minute += a[i] / j + (a[i] % j > 0 ? 1 : 0) - 1;
            }
            minute += j;
            
            if (res == 0 || res > minute) res = minute;
        }
        
        //cout << d << " " << a[0] << endl;
        cout << "Case #" << ti << ": " << res << endl;
    }
    cout.close();
}
