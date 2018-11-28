#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <cmath>

using namespace std;

long long change_base(int num, int from_base, int to_base) {
    long long result = 0;
    long long cur_base = 1;
    while (num > 0) {
        int last = num % from_base;
        result += last * cur_base;
        cur_base *= to_base;
        num /= from_base;
    }
    return result;
}

bool is_format(int num, int J) {
    if (num % 2 == 1) {
        int count = 0;
        int tmp = num;
        while (tmp > 0) {
            if ((tmp >> 1) > 0) {
                tmp >>= 1;
                count++;
            } else {
                return tmp == 1 && count == J - 1;
            }
        }
    }
    return false;
}

long long is_prime(long long num) {
    if ((num % 2) == 0) {
        return 2;
    }

    for (long long i = 3; i <= sqrt(num); i += 2) {
        if (i % 2 == 0)
            i++;

        if ((num % i) == 0) {
            return i;
        }
    }

    return 1;
}

bool is_correct(int num, int J) {
    if (!is_format(num, J)) {
        return false;
    }

    long long change_base_num[11];
    long long divisor[11];
    for (int i = 2; i < 11; i++) {
        change_base_num[i] = change_base(num, 2, i);
        divisor[i] = is_prime(change_base_num[i]);
        if(divisor[i] == 1) {
            return false;
        }
    }
    cout << change_base_num[10];
    for (int i = 2; i < 11; i++) {
        cout << " " << divisor[i];
    }
    cout << endl;
    return true;
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        int N, J;
        cin >> N >> J;
        int count = 0;
        cout << "Case #" << i << ": " << endl;
        for (int k = 3; k < 65536; k++) {
            if (count == J) {
                break;
            }

            if(is_correct(k, N)) {
                count++;
            }
        }

    }
    return 0;
}