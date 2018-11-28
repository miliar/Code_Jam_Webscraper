#include<iostream>
#include<algorithm>
using namespace std;

int d,p[2000];
int main()
{
    int T;
    freopen("b.out","w",stdout);
    cin >> T;
    for (int ii = 0; ii < T; ii++)
    {
        cout << "Case #" << ii + 1 << ": ";
        cin >> d;
        for (int i = 0; i < d; i++)
            cin >> p[i];
        sort(p,p + d);
        int p_max = p[d - 1];
        int best = 2000;
        for (int i = 1; i <= p_max; i++)
        {
            int ans = 0;
            for (int j = d - 1; j >= 0; j--)
            {
                if (p[j] >= i)
                    ans += p[j] / i - (p[j] % i == 0);
                else
                    break;
            }
            best = min(ans + i,best);
        }
        cout << best << endl;
    }
    return 0;
}
