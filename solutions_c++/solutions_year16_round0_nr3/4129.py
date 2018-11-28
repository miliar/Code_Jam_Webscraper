#include <iostream>
#include <string>
#include <bitset>
#include <math.h>
#include <vector>
#include <sstream>

using namespace std;

template <size_t N>
std::bitset<N> increment(bitset<N> in);

template <size_t N>
bool isCoinJam(bitset<N>, unsigned long long int (&divisors)[9]);

bool isPrime(unsigned long long int n, int base, unsigned long long int (&divisors)[9]);

unsigned long long int tobase(int n, bitset<16> in);

int main()
{
    unsigned long long int d = 0;
    unsigned long long int t;
    unsigned long long int n;
    unsigned long long int j;
    unsigned long long int divisors[9];
    vector<string> answer;

    cin >> t;
    cin >> n;
    cin >> j;

    for(int i = 0; i < 51; i++)
    {
        answer.push_back("");
    }

    string bits = "1";

    for(int i = 2; i < n; i++)
    {
        bits = bits + "0";
    }
    bits = bits + "1";

    std::bitset<16> x (bits);
    std::stringstream convertor;

    cout << "Case #1:" << endl;

    unsigned long long int b = 1;
    while(d < 49)
    {
        if(isCoinJam(x, divisors))
        {
            d = d + 1;
            convertor << x;
            //answer[d] = convertor.str();
            cout << x << " ";
            for(int k = 0; k < 9; k++)
            {
                cout << divisors[k] << " ";
            }
            cout << endl;
        }
        for(int i = 0; i < 9; i++)
        {
            divisors[i] = 0;
        }
        //b++;
        x = increment(x);
        //cout << "i successfully incremeanted" << endl;
    }
    bool onemore = true;
    while(onemore)
    {
        if(isCoinJam(x,divisors))
        {
            d = d + 1;
            convertor << x;
            //answer[d] = convertor.str();
            cout << x << " ";
            for(int k = 0; k < 9; k++)
            {
                cout << divisors[k] << " ";
            }
            cout << endl;
            onemore = false;
        }
        else
        {
            for(int i = 0; i < 9; i++)
            {
                divisors[i] = 0;
            }
            x = increment(x);
        }
    }
    //cout << "i got out" << endl;
}


template <size_t N>
bool isCoinJam(bitset<N> in, unsigned long long int (&divisors)[9])
{
    for(int i = 2; i <= 10; i++)
    {
        if(isPrime(tobase(i,in), i, divisors))
        {
            return false;
        }
    }
    //cout << in << endl;
    return true;
}

unsigned long long int tobase(int n, bitset<16> in)
{
    unsigned long long int total = 0;
    int c = 0;
    for ( size_t i = 0; i < 16; i++)
    {
        if(in[i] == 1)
        {
            total = total + pow(n,c);
        }
        c++;
    }
    return total;
}

bool isPrime(unsigned long long int n, int base, unsigned long long int (&divisors)[9])
{
    if(n < 2)
    {
        divisors[base - 2] = 1;
        return false;
    }
    if(n == 2) return true;
    if(n % 2 == 0)
    {
        divisors[base -2] = 2;
        return false;
    }
    for(int i=3; (i*i)<=n; i+=2){
        if(n % i == 0 )
        {
            divisors[base - 2] = i;
            return false;
        }
    }
    return true;
    /*
    //cout << "final boss" << endl;
    for(long int i = 2; i < n; i++)
    {
        if(n % i == 0)
        {
            cout << "do i ever" << endl;
            divisors[base - 2] = i;
            return false;
        }
    }
    cout << "please" << endl;
    return true;*/
}

template <size_t N>
std::bitset<N> increment ( std::bitset<N> in )
{
    //  add 1 to each value, and if it was 1 already, carry the 1 to the next.
    for ( size_t i = 0; i < N; ++i ) {
        if ( in[i] == 0 ) {  // There will be no carry
            in[i] = 1;
            break;
            }
        in[i] = 0;  // This entry was 1; set to zero and carry the 1
        }
        in[0] = 1;
    return in;
}
