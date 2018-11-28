#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void)
{
    int T; cin >> T;

    for (int t = 1; t <= T; t++)
    {
        int Smax; cin >> Smax;
        string Sstr; cin >> Sstr;
        
        int friends = 0;
        int tot = 0;
        for (int i = 0; i <= Smax; i++)
        {
            int S = Sstr[i] - '0';

            if (tot >= i)
                tot += S;
            else
            {
                //cout << i-tot << " friends needed at i=" << i << " and S=" << S << endl;
                friends += i-tot;
                tot = i+S;
            }
        }

        cout << "Case #" << t << ": " << friends << endl;
    }
}
