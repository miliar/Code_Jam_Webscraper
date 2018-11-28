#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long llu;

string plus_1(string s) {
    int i = s.length() - 2;
    s[i] += 1;
    while(s[i] == '2') {
        s[i] = '0';
        s[i - 1] += 1;
        i--;
    }
    return s;
}

int main() {
    int t, n, j;
    cin >> t;

    for(int c = 1 ; c <= t ; c++) {
        cin >> n >> j;

        cout << "Case #" << c << ":" << endl;

        // Sprawdzamy wszystkie liczby

        string num = "1";
        for(int i = 0 ; i < n - 2 ; i++)
            num += "0";
        num += "1";

        int cnt = 0;

        while(cnt < j) {
            // Sprawdzamy, czy ok
            llu num_int;
            vector<llu> provers;
            for(int base = 2 ; base <= 10 ; base++) {
                num_int = 1;
                llu mnoznik = base;
                for(int i = n - 2 ; i >= 0 ; i--) {
                    num_int += (num[i] - '0') * mnoznik;
                    mnoznik *= llu(base);
                }

                bool prime = true;
                for(llu x = 2 ; x * x <= num_int ; x++) {
                    if(num_int % x == 0) {
                        provers.push_back(x);
                        prime = false;
                        break;
                    }
                }

                if(prime == true)
                    break;
            }

            if(provers.size() == 9) {
                cnt++;
                cout << num;
                for(int i = 0 ; i < 9 ; i++)
                    cout << " " << provers[i];
                cout << endl;
            }

            num = plus_1(num);
        }
    }

    return 0;
}
