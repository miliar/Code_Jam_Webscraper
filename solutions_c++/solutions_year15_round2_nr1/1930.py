#include <iostream>
#include <algorithm>
#include <fstream>
#include <climits>
#include <vector>

using namespace std;

// partial specialization optimization for 32-bit numbers
int numDigits(int32_t x)
{
    if (x == LONG_MIN) return 10 + 1;
    if (x < 0) return numDigits(-x) + 1;

    if (x >= 10000) {
        if (x >= 10000000) {
            if (x >= 100000000) {
                if (x >= 1000000000)
                    return 10;
                return 9;
            }
            return 8;
        }
        if (x >= 100000) {
            if (x >= 1000000)
                return 7;
            return 6;
        }
        return 5;
    }
    if (x >= 100) {
        if (x >= 1000)
            return 4;
        return 3;
    }
    if (x >= 10)
        return 2;
    return 1;
}

template <typename T>
T expt(T p, unsigned q)
{
    T r(1);

    while (q != 0) {
        if (q % 2 == 1) {    // q is odd
            r *= p;
            q--;
        }
        p *= p;
        q /= 2;
    }

    return r;
}

int reverse(int num) {
    int new_num = 0;
    while(num > 0)
    {
            new_num = new_num*10 + (num % 10);
            num = num/10;
    }
    return new_num;
}

int main(void) {
    ifstream in ("A.in");
    ofstream out ("A.txt");
    int tests;
    in >> tests;
    cout << tests <<endl;
    for (int i=0; i < tests; i++) {
        //cout << "weszlo\n";
        int n;
        in >> n;
        vector<int> arr (n+1, LONG_MAX);
        arr[1] = 1;
        for (int i=1; i < n; i++) {
            arr[i+1] = min(arr[i+1],arr[i]+1);
            int rev = reverse(i);
            if (rev <= n) {
                arr[rev] = min(arr[rev], arr[i]+1);
            }
        }
        out << "Case #" << i+1 << ": " << arr[n] << endl;
    }
    in.close();
    out.close();
    return 0;
}
