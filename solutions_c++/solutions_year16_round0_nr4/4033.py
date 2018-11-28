#include <iostream>

using namespace std;

long longPow(long a, long b)
{
    long res = 1;
    for(long i = 0 ; i < b ; i++)
        res *= a;

    return res;
}

int main(int argc, char *argv[])
{
    long T, K, C, S;
    cin >> T;

    for(long i = 0 ; i < T ; i ++)
    {
        cin >> K >> C >> S;

        cout << "Case #" << i+1 << ": ";

        if(S < K)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            long pos =  longPow(K, C-1) / 2 + 1;
            cout << pos << " ";
            for(long longerval = 1 ; longerval < K ; longerval++)
            {
                pos += longPow(K, C-1);
                cout << pos << " ";
            }

            cout << endl;
        }

    }

    return 0;
}
