#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        string S;
        int K;
        int c = 0;
        cin >> S >> K;
        for (int i = 0; i <= S.size()-K; i++)
        {
            if (S[i] == '-')
            {
                c++;
                for (int j = i; j < i+K; j++)
                {
                    if (S[j] == '-')
                        S[j] = '+';
                    else
                        S[j] = '-';
                }
            }

        }
        bool ok = true;
        for (int i = S.size()-K+1; i < S.size(); i++)
        {
            if (S[i] == '-')
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            cout << "Case #" << t+1 << ": " << c << endl;
        }
        else
        {
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
        }
    }
}
