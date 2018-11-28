#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, c, S;
    string p;
    cin >> T;
    for (int c = 1; c <= T; c++)
    {
        cin >> S >> p;
        int need = 0;
        int sum = 0;
        for (int i = 0; i < p.length(); i++)
        {
            int lidi = p[i] - '0';
            if (lidi > 0 && need < i)
            {
                need = i;
            }
            need += lidi;
            sum += lidi;
        }
        cout << "Case #" << c << ": " << need-sum << endl;
    }
    return 0;
}
