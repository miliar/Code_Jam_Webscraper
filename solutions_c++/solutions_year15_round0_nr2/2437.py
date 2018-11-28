#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int main()
{
    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int D;

        cin >> D;

        vector<int> v;

        for (int j = 0; j < D; j++)
        {
            int in;

            cin >> in;

            v.push_back(in);
        }
        int count = 1001;

        for (int j = 1; j <= 1000; j++)
        {
            int aux = j;
            for (int k = 0; k < D; k++)
            {
                if (v[k] > j)
                {
                    aux += v[k] / j;

                    if (v[k] % j != 0)
                        aux++;

                    aux --;
                }
            }
            count = min(count, aux);
        }

        cout << "Case #" << i + 1 << ": " << count << endl;
    }
}
