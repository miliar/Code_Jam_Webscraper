#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, M, ANS;
    string S;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int tot = 0;
        ANS = 0;
        cin >> M >> S;
        if (M != 0)
        {
            tot += S[0] - 48;
            for(int i = 1; i <= M; i++)
            {
                if(tot >= i)
                    tot += S[i] - 48;
                else
                {
                    if(S[i] - 48 != 0)
                    {
                        ANS += i - tot;
                        tot += (i - tot) + (S[i] - 48);
                    }
                }
            }
        }
        cout << "Case #" << t << ": " << ANS << '\n';
    }
    return 0;
}
