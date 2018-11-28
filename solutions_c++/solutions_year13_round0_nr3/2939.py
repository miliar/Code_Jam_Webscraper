#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

bool isFair(long long num) {
    string strNum;
    ostringstream convert;
    convert << num;
    strNum = convert.str();
    bool pal = true;
    for (int i = 0; i < strNum.size() / 2; i++) {
        if (strNum[strNum.size() - 1 - i] != strNum[i]) {
            pal = false;
        }
    }
    return pal;
}

int main() {
    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        long long A, B;
        cin >> A >> B;
        long long res = 0;
        for (long long i = B; i >= A; i--) {
            if (isFair(i)) {
                long long r = sqrt(i);
                if (r*r == i) {
                    if (isFair(r)) {
                        res++;
                    }
                }
            }                
        }
        cout << "Case #" << x << ": " << res << endl;
    }
}