#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);

    int i = 0,T;  cin >> T;

    while(i++ != T)
    {
        int Sm; cin >> Sm;
        string S;   cin >> S;
        int Standed = 0, frnds = 0;

        for (int j = 0; j <=Sm; j++)
        {
	    if (S[j] == '0')
		continue;
            if (Standed >= j)
                Standed += (S[j] - '0');
            else
            {
                frnds += j - Standed;
                Standed += frnds + (S[j] - '0');
            }
        }
        cout << "Case #" << i << ": " << frnds << '\n';
    }
}
