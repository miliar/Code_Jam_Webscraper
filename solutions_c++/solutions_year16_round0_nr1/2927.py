#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;
typedef long long LL;

int main()
{
    int tries;
    long long N, result;
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("A-large.out", "w", stdout);
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        cin >> N;
        if (N == 0)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else
        {
            int multi = 1, sum;
            long long power;
            int arr[10];
            fill_n(arr,10,0);
            while (true)
            {
                sum = 0;
                power = 0;
                result = N*multi;
                power = result;
                while (power/10 > 0)
                {
                    arr[power%10] = 1;
                    power /= 10;
                }
                arr[power%10] = 1;
                for (int j = 0; j < 10; j++)
                    sum += arr[j];
                if (sum == 10)
                    break;
                multi++;
            }
            cout << "Case #" << i << ": " << result << endl;
        }
    }
    return 0;
}
