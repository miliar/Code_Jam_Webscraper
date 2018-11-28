#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int s, t;
    cin >> t;
    for (int j = 0; j < t; ++j)
    {
        cin >> s;
        //cerr << "  s = " << s << "\n";
        int cnt = 0, ans = 0;
        char c;
        for (int i = 0; i <= s; ++i)
        {
            cin >> c;
            //cerr << c;
            if (i <= cnt)
                cnt += (int)(c - '0');
            else
            {
                //cerr << i << " " << cnt << endl;
                ans += i - cnt;
                cnt = i;
                cnt += (int)(c - '0');
            }
        }
        //cerr << endl;
        cout << "Case #" << j+1 << ": " << ans << "\n";
    }


    return 0;
}
