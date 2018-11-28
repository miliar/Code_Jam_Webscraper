#include<iostream>
#include <set>

using namespace std;

int main() {
    int nCases, i = 1;
    cin >> nCases;
    while(nCases--) {
        int n;
        set<int> digits;
        cin >> n;
        if(n <= 0)
            cout << "Case #" << i++ << ": " << "INSOMNIA\n";
        else {
            int tmp = n, iter = 1;
            while(digits.size() < 10) {
                while(tmp) {
                    digits.insert(tmp % 10);
                    tmp /= 10;
                }
                tmp = (++iter) * n;
            }
            cout << "Case #" << i++ << ": " << (iter - 1) * n << endl;
        }
    }
    return 0;
}