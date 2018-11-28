#include <iostream>

using namespace std;

int main()
{
    long long a, b, k, t, cont = 0, l;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> a >> b >> k;

        for(int j = 0; j < a; j++)
        {
            for(int z = 0; z < b; z++)
            {
                for(int y = 0; y < k; y++)
                {
                    if((j&z) == y)
                    {
                        cont++;
                    }
                }
            }
        }

        cout << "Case #" << i+1 << ": " << cont << endl;
        cont = 0;
    }
    return 0;
}
