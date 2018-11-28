#include <fstream>

using namespace std;

const int MAXT = 200 + 10;
const int MAXN = 1e6 + 100;
int T, n;

int main()
{
    ios::sync_with_stdio(false);
    ifstream cin("input.in");
    ofstream cout("output.out");
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        cin >> n;
        cout << "Case #" << t + 1 << ": ";
        if (n == 0)
        {
            cout << "INSOMNIA\n";
            continue;
        }
        bool hasseen[10];
        for (int i = 0; i < 10; i++)
            hasseen[i] = 0;
        int numseen = 0;
        long long k = 0, c = 0;
        while (numseen < 10)
        {
            c += n;
            k = c;
            while (k)
            {
                int cur = k % 10;
                if (!hasseen[cur])
                    hasseen[cur] = true, numseen++;
                k /= 10;
            }
        }
        cout << c << '\n';
    }
    return 0;
}
