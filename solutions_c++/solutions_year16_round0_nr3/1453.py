#include <iostream>
#include <fstream>
#include <vector>
#include <gmp.h>

using namespace std;

void getNumber(mpz_t result, const mpz_t num, int basis, int N)
{
    mpz_set_ui(result, 0);
    mpz_t basisM;
    mpz_init_set_ui(basisM, basis);
    for (auto i = 0; i < N; i++)
    {
        mpz_t p;
        mpz_init(p);
        mpz_pow_ui(p, basisM, i);
        if (mpz_tstbit(num, i))
        {
            mpz_add(result, result, p);
        }
    }
}

unsigned long getDiv(const mpz_t num, int basis, int N)
{
    mpz_t number;
    mpz_init(number);
    getNumber(number, num, basis, N);
    for (unsigned long divisor = 2; divisor < 300; divisor++)
    {
        if (mpz_fdiv_ui(number, divisor) == 0)
        {
            return divisor;
        }
    }
    return 0;
}

void print(const mpz_t num, int N, ostream & cout)
{
    for (auto i = N-1; i >= 0; i--)
    {
        if (mpz_tstbit(num, i))
        {
            cout << "1";
        } else {
            cout << "0";
        }
    }

}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;
    fin >> T;

    for (auto t = 0; t < T; t++)
    {
        int N, J;
        fin >> N >> J;

        int count = 0;
        cout << "Case #" << (t+1) << ":" << endl;

        mpz_t two;
        mpz_init_set_ui(two, 2);

        mpz_t num;
        mpz_init(num);
        mpz_pow_ui(num, two, N - 1);
        mpz_add_ui(num,num, 1);

        mpz_t maxNum;
        mpz_init(maxNum);
        mpz_pow_ui (maxNum, two, N);

        for (;mpz_cmp(num, maxNum) < 0; mpz_add_ui(num, num, 2))
        {
            bool bad = false;
            vector<unsigned long> div;
            for (auto i = 2; i <= 10; i++)
            {
                auto result = getDiv(num, i, N);
                if (result == 0)
                {
                    bad = true;
                    break;
                }
                div.push_back(result);
            }

            if (!bad)
            {
                print(num, N, cout);
                cout << " ";
                for (auto i = 2; i <= 10; i++)
                {
                    cout << div[i-2];
                    if (i != 10)
                        cout << " ";
                }
                cout << endl;
                count ++;
            }
            if (count == J)
                break;
        }
    }

    return 0;
}
