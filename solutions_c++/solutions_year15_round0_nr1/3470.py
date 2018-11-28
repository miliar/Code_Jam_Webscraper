#include<iostream>
using namespace std;

int main()
{
    int T;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin >> T;
    for (int ii = 0; ii < T; ii++)
    {
        cout << "Case #" << ii + 1<<": ";
        int smax;
        string level;
        cin >> smax >> level;
        int ans = 0 , cur = 0;
        for (int i = 0; i <= smax; i++)
        {
            if (cur < i)
            {
                ans += i - cur;
                cur = i;
            }
            cur += level[i] - '0';
        }
        cout << ans << endl;
    }
    return 0;
}
