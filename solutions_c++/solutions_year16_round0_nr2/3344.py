//Eldar Gaynetdinov

#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;

    for(int t = 1; t <= T; t++)
    {
        string S; cin >> S;

        uint64_t z, o;

        if(S.front() == '+')
        {
            z = 1;
            o = 0;
        }
        else
        {
            z = 0;
            o = 1;
        }

        for(unsigned i = 1; i < S.length(); i++)
        {
            char c = S[i];

            if(c == '+')
            {
                uint64_t tmp_z = min(o + 1, z + 2);
                uint64_t tmp_o = min(o,     z + 1);

                z = tmp_z; o = tmp_o;
            }
            else
            {
                uint64_t tmp_z = min(o + 1, z);
                uint64_t tmp_o = min(o + 2, z + 1);

                z = tmp_z; o = tmp_o;
            }
        }

        cout << "Case #" << t << ": " << o << endl;
    }

    return 0;
}
