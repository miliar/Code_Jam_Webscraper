#include <iostream>
using namespace std;

long long unsigned int allDigitsSeen(long long unsigned int n)
{
    if(n == 0)
        return 0;

    long long unsigned int additive = n;
    int digitsSeen = 0;
    bool seen[10] = {false};

    while(digitsSeen < 10)
    {
        long long unsigned int m = n;
        while(m > 0)
        {
            int digit = m % 10;
            m /= 10;
            if(!seen[digit])
            {
                seen[digit] = true;
                digitsSeen++;
            }
        }

        n += additive;
    }

    return (n - additive);
}

int main()
{
    int t, n;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>n;
        if(n == 0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i<<": "<<allDigitsSeen(n)<<endl;
    }

    return 0;
}
