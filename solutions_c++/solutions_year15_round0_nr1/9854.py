#include<iostream>

using namespace std;

int main()
{
    int T;
    int smax;
    string s;

    while (cin >> T)
    {
        for (int i = 1; i <= T; i++)
        {
            int convidados = 0;
            int empe = 0;
            cin >> smax >> s;

            for(int k = 0; k <= smax; k++)
            {
                if(empe >= k || (s[k] -'0') == 0)
                    empe += s[k]- '0';
                else
                    empe += s[k] -'0' + (convidados += k - empe);
            }
            cout << "Case #" << i << ": " << convidados <<endl;
        }
    }
    return 0;
}
