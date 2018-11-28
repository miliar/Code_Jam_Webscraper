#include <iostream>
#include <bitset>
#include <cmath>
#include <cstring>

using namespace std;

int sum[11] = {0,};

int main()
{
    cout << "Case #1:" << endl;

    for (int i=0; i<50; ++i) {
        bitset<6> s(i);

        for (int j=15; j>=0; --j) {
            if (j>=1 && j<=6) {
                cout << s[j-1];
            } else if (j>=9 && j<=14) {
                cout << s[j-9];
            } else {
                cout << "1";
            }
        }

        memset(sum, 0, sizeof(int)*11);
        for (int j=2; j<=10; ++j) {
            sum[j] += pow(j,7) + 1;
            for (int k=s.size()-1; k>=0; --k) {
                if (s[k]) {
                    sum[j] += pow(j,k+1);
                }
            }
            cout << " " << sum[j];
        }
        cout << endl;
    }
}
