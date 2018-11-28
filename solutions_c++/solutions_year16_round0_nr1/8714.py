#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
typedef unsigned long long ULL;

void tackleNext(unsigned int& freq, ULL x)
{
    do {
        freq = freq | 1 << x%10;
        x /= 10;
    } while (x);
}

ULL run(int val)
{
    const unsigned int mask = 0b1111111111;
    unsigned int freq = 0;
    if (val == 0)
        return 0;
    ULL x = static_cast<ULL>(val);
    const ULL n = x;
    ULL prev = 0;
    ULL i = 1;
    do
    {
        tackleNext(freq, x);
        if (freq == mask) // int overflow
            return x;
        prev = x;
        x += n;
        ++i;
    } while (x > prev);
    return 0;
}

int main(int nargs, char** args)
{
    //cout << "BB = " << run(2);
    //ps("", mask);
    //ps("", freq);
    //cout << (freq == mask) << "\n";
    //return 0;

    int nsamples = 0;
    ifstream infile("A-large.in");
    
    infile >> nsamples;

    vector<int> samples(nsamples, 0);
    for (int i = 0; i < nsamples; ++i) {
        infile >> samples[i];
        if (samples[i] < 0)
            samples[i] *= -1;
    }

    ofstream outfile("test.out");
    for (int i = 0; i < nsamples; ++i) {
        ULL res = run(samples[i]);
        outfile << "Case #" << i+1 << ": ";
        if (res != 0)    
            outfile << res << "\n";
        else
            outfile << "INSOMNIA\n";
    }

    return 0;
}
