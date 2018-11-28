#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int t = 0;
    cin >> t;
    for (int s=1; s<=t; ++s)
    {
        int fst_ans = 0;
        int sec_ans = 0;
        int fst_arr[5][5] = {0};
        int sec_arr[5][5] = {0};
        int res = 0;
        int ans = 0;

        cin >> fst_ans;
        for (int i=1; i<=4; ++i)
        {
            for (int j=1; j<=4; ++j)
            {
                cin >> fst_arr[i][j];
            }
        }
        cin >> sec_ans;
        for (int i=1; i<=4; ++i)
        {
            for (int j=1; j<=4; ++j)
            {
                cin >> sec_arr[i][j];
            }
        }

        for (int i=1; i<=4; ++i)
        {
            for (int j=1; j<=4; ++j)
            {
                if (fst_arr[fst_ans][i] == sec_arr[sec_ans][j])
                {
                    res += 1;
                    ans = fst_arr[fst_ans][i];
                }
            }
        }
        if (res == 0) cout << "Case #" << s << ": " << "Volunteer cheated!" << endl;
        else if (res == 1) cout << "Case #" << s << ": " << ans << endl;
        else cout << "Case #" << s << ": " << "Bad magician!" << endl;
    }
    return 0;
}
