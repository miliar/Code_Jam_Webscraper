#include <iostream>
#include <fstream>
using namespace std;
const int MAXN = 32;
const int nPRIME = 101;
const int MAX_BASE = 10, MIN_BASE = 2;
ifstream fin;
ofstream fout;
int T;
    int N;
    int J;
int proove_div[MAX_BASE + 1];
int coin[MAXN];
int Primes[nPRIME] =
{
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
    467,
    479,
    487,
    491,
    499,
    503,
    509,
    521,
    523,
    541,
    547
};


void start_coin() {
    for (int i = 0; i < N; ++i)
    {
        coin[i] = 0;
    }
}
bool next_coin() {
    int j = 0;
    for (;j < N; ++j)
    {
        if (coin[j])
        {
            coin[j] = 0;
        }
        else
        {
            coin[j] = 1;
            return false;
        }
    }
    return j == N;
}

void start ()
{
    start_coin();
}

int check_is_base (int p)
{
    int cur_rem;
    int cur_prime;
    int cur_p;
    for (int i = 0; i < nPRIME; ++i)
    {
        cur_p = p;
        cur_rem = 1;
        cur_prime = Primes[i];
        for (int j = 0; j < N; ++j)
        {
            cur_rem = (cur_rem + coin[j] * cur_p) % cur_prime;
            cur_p = cur_p * p % cur_prime;
        }
        cur_rem = (cur_rem + cur_p) % cur_prime;
        if (cur_rem == 0) return cur_prime;
    }
    return 0;
}
bool check_coin ()
{
    int base_prover;
    for (int base = MIN_BASE; base <= MAX_BASE; ++base)
    {
        base_prover = check_is_base(base);
        if (base_prover == 0)
        {
            return true;
        }
        proove_div[base] = base_prover;
    }
    return false;
}

bool search_next_coin ()
{
    while (check_coin())
    {
        if (next_coin())
        {
            //cerr << "not enough primes!" << endl;
            return true;
        }
    }
    return false;
}

void print_coin ()
{
    fout << 1;
    for (int i = N - 1; i >= 0; --i)
    {
        fout << coin[i];
    }
    fout << 1;
}

void print_proov ()
{
    for (int base = MIN_BASE; base <= MAX_BASE; ++base)
    {
        fout << " " << proove_div[base];
    }
}
int main(int argc, char * argv[]) {

    fin.open(argv[1]);
    fout.open(argv[2]);

    fin >> T;
    for (int i = 1; i <= T; ++i)
    {
        fin >> N >> J;
        N -= 2;
        fout << "Case #" << i << ":" << endl;
        start();
        int j = 0;
        if (!check_coin())
        {
            print_coin();
            print_proov();
            fout << endl;
            next_coin();
            ++j;
        }
        for (; j < J; ++j)
        {
            if (search_next_coin())
            {
                break;
            }
            print_coin();
            print_proov();
            fout << endl;
            next_coin();
        }
    }
    return 0;
}
