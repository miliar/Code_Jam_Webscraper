#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int T;
string S;
int R, C, Smx;

int main()
{
    //freopen("input_large.txt", "r", stdin);
    //freopen("output_large.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> Smx;
        cin >> S;
        R = 0;
        C = 0;
        for (int i = 0; i < S.length(); ++i)
            if (S[i] != '0')
            {
                if (C >= i) C += (int)(S[i] - '0');
                else
                {
                    R += i - C;
                    C += (i - C) + (int)(S[i] - '0');
                }
            }
        cout << "Case #" << t << ": " <<  R << endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
