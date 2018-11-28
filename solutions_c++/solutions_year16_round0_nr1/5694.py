#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

//    freopen("t.in", "r", stdin);
//    freopen("t.out", "w", stdout);
    int nbT;
    cin >> nbT;
    for (int t = 1; t <= nbT; t++)
    {
        long long n;
        cin >> n;

        long long x = 0;
        if (n != 0)
        {
            vector<bool> seen(10, false);
            int nbSeen = 0;
            while (nbSeen != 10)
            {
                x += n;
                long long x2 = x;
                while (x2 != 0)
                {
                    int a = x2%10;
                    if (!seen[a])
                    {
                        seen[a] = true;
                        nbSeen++;
                    }
                    x2/=10;
                }
            }
        }





        cout << "Case #" << t << ": ";

        if (n == 0)
            cout << "INSOMNIA\n";
        else
            cout << x << '\n';

    }

    return 0;
}
