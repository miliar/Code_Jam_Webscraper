#include <iostream>
#include <bitset>
#include <cmath>
#include <cstring>
#include <vector>
#include <iomanip>
#include <sstream>

using namespace std;

int is_prime(long int N)
{
    if(N <= 1) return 0;

    for(int i = 2, sqrt_N = sqrt(N); i <= sqrt_N; i++)
        if(N % i == 0)
            return 0;
    return 1;
}

long int get_num(string &s, int base, int size) {

    long int ret = 0;
    long int multi = 1;

    for(int i = 15; i >= 15-size; i--)
    {/////////////////////15555555555555555555
        if(s[i] == '1')
            ret += multi;

        multi *= base;
    }

    return ret;
}


int main()
{

    string curr_bits_config;

    int T, N, J; cin >> T >> N >> J;
    long int number;

    long int bases[11];
    int divisors[11];
    bool current_num_is_prime;
    for(int t = 1; t <= T; ++t)
    {
        cout << "Case #" << t << ':' << endl;
        for(int i = pow(2, N-1),  n = pow(2, N); i < n; ++i)
        {

            bitset<16> bin(i);
            curr_bits_config = bin.to_string();

            if(!(curr_bits_config[15] == '1')) continue;

            for(int j = 2; j <= 10; ++j)
            {

                bases[j] = get_num(curr_bits_config, j, N);
                current_num_is_prime = is_prime(bases[j]);
                if(current_num_is_prime)
                {
                    break;
                }

            }
            if(current_num_is_prime) continue;

            for(int j = 2; j <= 10; ++j)
            {
                for(int k = 2; k < bases[j]; ++k)
                    if(bases[j] % k == 0)
                    {
                        divisors[j] = k;
                        break;
                    }

            }

            cout << curr_bits_config;
            for(int j = 2; j <= 10; j++)
            {
                cout << ' ' << divisors[j];
            }

            cout << endl;

            if(--J == 0) break;

            // cout << curr_bits_config << ' ';
            // for(int j = 2; j <= 10; ++j)
            // {
            //     cout << bases[j] << ' ';
            // }
            // cout << endl;

        }
    }

    return 0;

}
