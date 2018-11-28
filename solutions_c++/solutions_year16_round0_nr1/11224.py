#include <iostream>
#include <random>
#include <iomanip>
#include <vector>
using namespace std;

int main()
{
    long long TC, N;
    cin >> TC;
    long long k = 1;

    while(TC--)
    {
        vector<bool> dac(10, 0);
        cout << "Case #" << k++ << ": ";
        cin >> N;

        if (N == 0) {
            cout << "INSOMNIA" << endl;
        }
        else{
            long long last;
            long long i = 1;
            while(find(dac.begin(), dac.end(), false) != dac.end())
            {
                long long a = i * N;
                last = a;
                while(a)
                {
                    dac[a%10] = true;
                    a/=10;
                }
                i++;
            }
            cout << last << endl;
        }
    }

    return 0;
}
