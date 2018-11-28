#include<iostream>
#include<vector>
using namespace std;

int countUntil(int n) {
    vector<bool> allDigits (10, false);
    int hit = 0;

    int curn = n;
    while (true) {
        int tmp = curn;
        while(tmp) {
            if (!allDigits[tmp%10]) {
                allDigits[tmp%10] = true;
                hit ++;
            }
            tmp = tmp / 10;
        }
        if (hit == 10) {
            return curn;
        }
        curn += n;
    }
}

int main() {
    int t,n;
    cin >> t ;
    for(int i=0; i < t; i++) {
        cin >> n;
        if (n == 0) {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << countUntil(n) << endl;
        }
    }
    return 0;
}
