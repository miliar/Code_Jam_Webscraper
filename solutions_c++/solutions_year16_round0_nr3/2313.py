#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <string>
#include <climits>
#include <algorithm>

using namespace std;

long long isPrime(long long n)
{
    if(n <= 1) return -1;
    if(n == 2) return -1;
    if(n % 2 == 0) return 2;
    long long m = sqrt(n);
    for(long long i = 3; i <=m; i += 2)
    {
        if(n % i == 0)
        {
            return i;
        }
    }
    return -1;
}

string toBin(long long in)
{
    string ret = "";
    while(in > 0)
    {
        ret.push_back((in & 1)+ '0');
        in = in >> 1;
    }
    reverse(ret.begin(),ret.end());
    return ret;
}


int main()
{
    long long out[11];
    long long start = 1;
    string in;
    start = start << 15;
    start++;
    bool good = false;
    int counter = 0;
    cout << "Case #1:" << endl;
    while(counter < 50)
    {
        good = true;
        for(int i = 2; i <= 10 && good; i++)
        {
            in = toBin(start);
            out[i] = isPrime(stoll(in,nullptr,i));
            if(out[i] == -1)
            {
                good = false;
            }
        }
        if(good)
        {
            cout << in << " ";
            for(int i = 2;i <= 10; i++)
            {
                cout << out[i];
                if(i != 10)
                {
                    cout << " ";
                }
            }
            cout << endl;
            counter++;
        }
        start += 2;

    }

}
