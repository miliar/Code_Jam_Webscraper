#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        vector<int> v;

        for (int i = 0; i < n; i++)
        {
            int in;
            cin >> in;
            v.push_back(in);
        }

        int out1 = 0;
        int out2 = 0;

        int difMax = 0;


        for (int j = 1; j < n; j++)
        {
            int atual = v[j - 1];
            int prox = v[j];

            if (atual > prox)
            {
                int dif = atual - prox;

                out1 += dif;

                difMax = max(difMax, dif);
            }

        }

        for (int j = 0; j < n - 1; j++)
        {
            if (v[j] < difMax)
                out2 += v[j];
            else out2 += difMax;
        }

        cout << "Case #" << i + 1 << ": " << out1 << " " << out2 << endl;
    }
}
