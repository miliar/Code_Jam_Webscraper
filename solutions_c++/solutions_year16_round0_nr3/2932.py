#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
typedef unsigned long long ull;

void generate_divisors_and_primes(
    unordered_map<ull, ull>& divisors,
    vector<ull>& primes,
    int primes_size
) {
    primes[0] = 2;
    primes[1] = 3;
    int count = 2;

    ull next_prime = primes[1];
    while (count < primes_size)
    {
        next_prime += 2;
        bool is_prime = true;
        for (int i = 0; i < count && primes[i] <= sqrt(next_prime); i ++)
        {
            if (next_prime % primes[i] == 0)
            {
                divisors[next_prime] = primes[i];
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            divisors[next_prime] = 1;
            primes[count ++] = next_prime;
        }
    }
}

ull convert_to_base_10(ull number, int base)
{
    if(number == 0 || base == 10)
        return number;

    return number % 10 + base * (convert_to_base_10(number / 10, base));
}

bool is_prime(
    ull nr,
    ull& divisor,
    const vector<ull>& primes,
    unordered_map<ull, ull>& divisors
) {
    if (! (nr & 1)) { // even
        divisor = 2;
        return false;
    }
    if (divisors[nr] == 1) // precomputed && prime
        return true;
    if (divisors[nr] != 0) { // precomputed && not prime
        divisor = divisors[nr];
        return false;
    }

    int i = 0;
    ull potential_divisor = primes[i];
    ull sqrt_nr = ceil(sqrt(nr));
    while (potential_divisor <= sqrt_nr)
    {
        if (nr % potential_divisor == 0)
        {
            divisor = potential_divisor;
            divisors[nr] = divisor;
            return false;
        }

        if (i + 1 < primes.size()) {
            potential_divisor = primes[++i];
        } else {
            potential_divisor += 2;
        }
    }

    divisors[nr] = 1;
    return true;
}

// returns true if all j elements were found
bool find_legitimate(
    ull nr,
    int& found,
    int j,
    const vector<ull>& primes,
    unordered_map<ull, ull>& divisors
) {

    vector<ull> base_divisors(9);
    for (int i = 2; i <= 10; i ++) {
        ull curr_base = convert_to_base_10(nr, i);
        if (is_prime(curr_base, base_divisors[i - 2], primes, divisors)) {
            return false;
        }
    }

    cout << nr;
    for (int i = 0; i < 9; i ++)
        cout << " " << base_divisors[i];
    cout << endl;

    if (found == j - 1) {
        return true;
    }
    found ++;

    return false;
}

void solve(int test_nr)
{
    int n, j;
    cin >> n >> j;

    cout << "Case #" << test_nr << ":" << endl;

    const int primes_size(1e5); // how many primes we want to precompute
    vector<ull> primes(primes_size, 0);
    // divisors[i] == j -> j is a divisor of i (1 if prime)
    unordered_map<ull, ull> divisors;
    generate_divisors_and_primes(divisors, primes, primes_size);

    int found = 0;
    unsigned long long start = 1 + pow(10, n - 1);
    vector<ull> all (1, start);
    find_legitimate(start, found, j, primes, divisors);
    for (int i = 1; i < n - 1; i ++)
    {
        int initial_size = all.size();
        for (int k = 0; k < initial_size; k ++)
        {
            ull new_nr = all[k] + pow(10, i);
            if (find_legitimate(new_nr, found, j, primes, divisors))
                return;

            all.push_back(new_nr);
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i ++) {
        solve(i);
    }

    return 0;
}
