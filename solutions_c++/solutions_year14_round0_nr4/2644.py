#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;

    for (int tt = 0; tt < T; ++tt)
    {
        int N;
        cin >> N;
        std::vector<double> naomi(N, 0);
        std::vector<double> ken(N, 0);

        for (int i = 0; i < N; ++i)
        {
            cin >> naomi[i];
        }
        for (int i = 0; i < N; ++i)
        {
            cin >> ken[i];
        }

        int dp = 0;
        int p = 0;

        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        int j = N - 1;
        for (int i = N-1; i >= 0; --i)
        {
            if (naomi[i] > ken[j])
            {
                ++ p;
            } else 
            {
                -- j;
            }
        }

        j = N - 1;
        for (int i = N-1; i >= 0; --i)
        {
            if (naomi[j] > ken[i])
            {
                ++ dp;
                -- j;
            }
        }

        cout << "Case #" << tt+1 << ": "
             << dp << " " << p << endl;
    }
    return 0;
}