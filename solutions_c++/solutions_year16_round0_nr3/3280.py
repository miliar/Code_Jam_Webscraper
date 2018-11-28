#include <iostream>
#include <string>
#include <set>
#include <cmath>
#include <deque>
#include <bitset>
#include <vector>
#include <set>

using namespace std;
int found = 0;
int required;
long long get_divisor(long long N)
{
    long long sqrt_N;

    for (int i = sqrt(N); i > 2; i--) {
        if (N % i == 0)  return i;
    }

    return -1;
}

long long value_decimal(unsigned bits, int base) {
    long long value = 0;
    long long power = 1;

    for (int i = 0; i < 32; i++) {
        if (i == 0) value += bits & 1;
        else value += ((bits & (1 << i)) >> i) * power;

        power *= base;
    }

    return value;
}

set<int> seen;

void generate_and_test(unsigned bits, int position, int size)
{
    bool jamcoin = true;
    static vector<long long> bases(9, 0);
    

    if (seen.find(bits) == seen.end()) {
        for (int i = 2; i <= 10; i++) {
            bases[i - 2] = get_divisor(value_decimal(bits, i));

            if (bases[i - 2] < 0) {
                jamcoin = false;
                break;
            }
        }

        if (jamcoin) {
            
            cout << value_decimal(bits, 10);
            for (int i = 0; i < 9; i++) cout << " " << bases[i];

            cout << endl;
            
            found++;

            if (found == required) return;
        }
    }

    seen.insert(bits);

    if ((position + 1) == (size - 1)) return;

    generate_and_test(bits + (1 << (position + 1)) , position + 1, size);

    if (found == required) return;

    generate_and_test(bits, position + 1, size);
    
    if (found == required) return;
}

int main()
{
    int T;
    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++) {
        int N, J;
        unsigned bits = 0;

        std::cin >> N;
        std::cin >> J;
        std::cout << "Case #" << idx << ":" << std::endl;

        found = 0;
        required = J;

        bits = 1 + (1 << (N - 1));

        generate_and_test(bits, 1, N);
        if (found == required) continue;
        generate_and_test(bits + 2, 1, N);
    }

    return 0;
}

