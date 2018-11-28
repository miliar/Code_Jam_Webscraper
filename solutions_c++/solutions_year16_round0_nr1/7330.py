#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

unsigned long long get_max(unsigned long long n) {
    n *= 10;
    auto curr = n;

    int digit = 0;

    while (n != 0) {
        digit++;
        n /= 10;
    }

    return curr * pow(10, digit);
}

void print_count(vector<bool> existed) {
    for (int i = 0; i < existed.size(); ++i)
        printf("%c", existed[i] ? 'T': 'F');
    cout << endl;
}



void count(unsigned long long n, vector<bool>& existed) {
    /*
    printf("Before: ");
    print_count(existed);

    printf("After %lld: ", n);
    */

    while (n != 0) {
        existed[n % 10] = true;
        n /= 10;
    }

    //print_count(existed);
}

long long solve(unsigned long long n) {
    if (n == 0)
        return -1;
    if (n == 1)
        return 10;

    auto curr = n;
    vector<bool> existed(10, false);

    unsigned long long n_max = get_max(n);

    count(curr, existed);

    for (int i = 0; i < existed.size(); ++i) {
        if (existed[i])
            continue;

        if (curr >= n_max)
            return -1;

        while (curr < n_max && existed[i] == false) {
            curr += n;
            count(curr, existed);
        }
    }

    return curr;
}

int main() {
    int T;
    cin >> T;

    for (int k = 1; k <= T; ++k) {
        unsigned long long N;
        cin >> N;

        auto ret = solve(N);

        if (ret == -1) {
            printf("Case #%d: INSOMNIA\n", k);
        }
        else {
            printf("Case #%d: %lld\n", k, ret);
        }
    }
}
