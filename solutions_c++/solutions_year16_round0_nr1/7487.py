#include <iostream>

using namespace std;

int main() {

    int k;
    cin >> k;
    for (int i = 1; i <= k; ++i) {
        int n;
        cin >> n;
        if(n != 0) {
            long long mult = 0;
            int nums = 0;
            while(nums != 1023) {
                mult++;
                long long tmp = n*mult;
                while(tmp > 0) {
                    nums = nums|(1<<(tmp%10));
                    tmp /= 10;
                }
            }
            cout << "Case #" << i << ": " << n*mult << endl;
        } else {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
    }

    return 0;
}