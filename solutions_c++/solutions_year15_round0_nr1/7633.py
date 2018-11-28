#include <bits/stdc++.h>

using namespace std;

int toInt(char ch)
{
    return ch - '0';
}

int main()
{

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T, Smax;
    string dig;

    cin >> T;

    for(int i = 1; i <= T; i++)
    {
        cin >> Smax >> dig;

        int stand = 0, need = 0;

        stand = stand + toInt(dig[0]);;

        int sz = dig.size()-1;

        for(int j = 1; j <= sz; j++)
        {
            if(dig[j] > 0)
            {
                if(stand >= j)
                {
                    stand = stand + toInt(dig[j]);
                }
                else
                {
                    int t = j - stand;
                    need = need + t;

                    stand  = stand + t + toInt(dig[j]);

                }
            }

        }

        cout << "Case #" << i << ": " << need << endl;
    }


    return 0;
}
