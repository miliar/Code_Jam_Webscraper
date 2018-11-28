#include <iostream>
#include <map>
using namespace std;

void getDigitsOfNumAndAddToMap(map<int, int>& mapp, int num) {
    int temp = num;
    while(temp != 0) {
        int mod = temp %10;
        temp = temp /10;
        mapp[mod]++;
    }
}

bool checkIfAllDigitsPresent(map<int, int>& mapp) {
   for(int i = 0; i<=9; ++i) {
        if (mapp[i] == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    int t, n, m;
    cin >> t;  // read t.
    for (int i = 1; i <= t; ++i) {
        cin >> n;  // read n
        int num = n;
        int factor = 2;
        map<int, int> mapp;
        while (1) {
            if (n==0) {
                break;
            }
            getDigitsOfNumAndAddToMap(mapp, n);
            if (checkIfAllDigitsPresent(mapp) == true) {
                break;
            } else {
                n = num * factor;
                factor++;
            }
        }
        if (n == 0) {
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        } else {
            cout << "Case #" << i << ": " << n << endl;
        }
   }
}
