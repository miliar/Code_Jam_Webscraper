#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    string nap;
    for (int i = 0; i < T; ++i)
    {
        int n;
        string nap;
        cin >> n >> nap;
        int il_kl = 0, il_dod = 0;
        for (int j = 0; j < n + 1; ++j)
        {
            if ((int) (nap[j] - 48) != 0)
            {
                if (il_kl < j)
                {
                    il_dod += (j - il_kl);
                    il_kl = j + (int) (nap[j] - 48);
                }
                else il_kl += (int) (nap[j] - 48);
            }
        }
        cout << "Case #" << i + 1 << ": " << il_dod << endl;
    }
    return 0;
}
