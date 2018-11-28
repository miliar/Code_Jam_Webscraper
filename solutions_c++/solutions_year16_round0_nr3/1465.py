#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <ctime>
#include <cstdlib>
#include <cmath>

using namespace std;

string gen_good_jamcoin(int l, set<string> &jamcoins)
{
    // generate a random "half" jamcoin and concatenate it to  itself to make full.
    int L = l/2;
    string jamcoin;
    for (int i=0; i<L; ++i)
    {
        jamcoin.push_back('0');
    }
    jamcoin[0] = '1';
    jamcoin[L-1] = '1';

    int ones = rand() % 10 + 1;
    int N_POS = L - 2;
    while (ones--)
    {
        int j = rand() % N_POS + 2;
//        cout << j << " " << ones << endl;
        if ( jamcoin[j] == '1') ones++;
        jamcoin[j] = '1';
    }

    if (! jamcoins.insert(jamcoin).second )
    {
//        cout << "Re-generated: " << jamcoin << endl;
//        cout << "Trying again!" << endl;
        return gen_good_jamcoin(l, jamcoins);
    }
    else
        return jamcoin.append(jamcoin);
}

/* Logic

Each 2^32 bit number, that is symmetric around centre is divisible by k^16 + 1
So we can just generate any random number that is symmetric along centre, and it will be composite, with (k^16 + 1) as factor.
Also, a symmetric base, with even 1's implies number is always divisible by 2.
*/

int main()
{
    int t;
    cin >> t;


    srand (time(NULL));

    for (int c=1; c<=t; ++c)
    {
        int N, J;
        cin >> N;
        cin >> J;

        int base_arr[] = {2,3,4,5,6,7,8,9,10};
        vector<int> bases (base_arr, base_arr + sizeof(base_arr) / sizeof(int) );

        /*

        > 2^16+1
        65537
        > 4^16+1
        4294967297
        > 6^16+1
        2821109907457
        > 8^16+1
        281474976710657
        > 10^16+1
        10000000000000001

        factor 4294967297
        4294967297: 641 6700417

        factor 2821109907457
        2821109907457: 353 1697 4709377

        factor 281474976710657
        281474976710657: 193 65537 22253377

        factor 10000000000000001
        10000000000000001: 353 449 641 1409 69857

        */

        int divisor_arr[] = {65537, 2, 641, 2, 353, 2, 193, 2, 353 };
        vector<int> divisors (divisor_arr, divisor_arr + sizeof(divisor_arr) / sizeof(int) );


        // Now serially generate
        set<string> jamcoins;
        cout << "Case #" << c << ": " << endl;

        for (int i=0; i<J; ++i)
        {
            string jamcoin = gen_good_jamcoin(N,jamcoins);
            cout << jamcoin;
            for (int i = 0; i < divisors.size(); ++i)
            {
                cout << ' ' << divisors[i];
            }
            cout << endl;
        }


    }
    return 0;
}
