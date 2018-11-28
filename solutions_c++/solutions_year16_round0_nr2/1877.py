#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

const int MAXN = 100;

int cnt[MAXN + 1][MAXN + 1];

int main()
{
    int t, kaseno = 0;
    cin >> t;
    while(t--)
    {
        string str;
        cin >> str;
        cout << "Case #" << ++kaseno << ": ";
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < str.size(); i++)
        {
            for (int j = 0; j <= str.size(); j++)
                cnt[i][j] = INT_MAX;
        }
        if (str[0] == '-')
            cnt[0][0] = 0, cnt[0][1] = 1;
        else
            cnt[0][0] = 1, cnt[0][1] = 0;
        for (int i = 1; i < str.size(); i++)
        {
            for (int j = 0; j <= i; j++)
            {
                if (str[i] == '+')
                {
                    cnt[i][j + 1] = min(cnt[i - 1][j], cnt[i][j + 1]);
                    cnt[i][i - j] = min(cnt[i][i - j], cnt[i - 1][j] + 1);
                }
                else
                {
                    cnt[i][j] = min(cnt[i - 1][j], cnt[i][j]);
                    cnt[i][i - j + 1] = min(cnt[i - 1][j] + 1, cnt[i][i - j + 1]);
                }
            }
        }
        cout << cnt[str.size() - 1][str.size()] << endl;
    }
    return 0;
}