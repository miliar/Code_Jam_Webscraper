#include <iostream>
#include <cstdio>

using namespace std;

string const noans = "INSOMNIA";

int main() {
    freopen("./large.in", "r", stdin);
    freopen("./large.out", "w", stdout);

    int t;
    cin >> t;

    for (int i=1; i<=t; ++i) {
        long long num;
        cin >> num;
        if (num == 0) {
            cout << "Case #" << i << ": " << noans << "\n";
        }
        else {
            bool seen[10];
            for (int index=0; index<=9; ++index) {
                seen[index] = false;
            }
            bool done = false;
            long long current = 0;
            while(!done) {
                current += num;
                long long temp = current;
                while (temp > 0) {
                    seen[temp % 10] = true;
                    temp = temp / 10;
                }
                bool isdone = true;
                for (int index=0; index<=9; ++index) {
                    if (!seen[index]) {
                        isdone = false;
                    }
                }
                done = isdone;
            }
            cout << "Case #" << i << ": " << current << "\n";
        }
    }

    return 0;
}
