#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //ifstream cin ("prob1.inp");
    //ofstream cout ("prob1.out.1");
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int test;
    cin >> test;
    for (int ttest = 1; ttest <= test; ttest++)
    {
        cout << "Case #" << ttest << ": ";
        int n;
        cin >> n;
        int ans = 0;
        string s;
        cin >> s;
        int cnt = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (i > cnt)
            {
                int tmp = i - cnt;
                cnt += tmp;
                ans += tmp;
            }
            cnt += s[i] - '0';
        }
        cout << ans << "\n";
    }
}
