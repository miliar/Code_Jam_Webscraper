#include <iostream>
#include <stdio.h>
#include <cstring>
#include <climits>
#include <cmath>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
    {
        int ret = 0;
        int flag = 1;
        int cnt[102][102] = {0};
        int ord[102][102] = {0};
        int N;
        cin >> N;
        string s;
        for (int i=0; i<N; ++i)
        {
            cin >> s;
            int idx = 1;
            for (int j=0; j<s.length(); ++j)
            {
                if (ord[i][idx] == 0)
                {
                    ord[i][idx] = s[j]-'a'+1;
                    cnt[i][idx] += 1;
                }
                else if (ord[i][idx] != 0)
                {
                    if (ord[i][idx] == s[j]-'a'+1) cnt[i][idx] += 1;
                    else
                    {
                        idx += 1;
                        ord[i][idx] = s[j]-'a'+1;
                        cnt[i][idx] += 1;
                    }
                }
            }
            ord[i][0] = idx;
        }
        for (int i=1; i<N; ++i)
        {
            for (int j=0; j<=ord[i][0]; ++j) {
                if (ord[i][j] != ord[0][j]) flag = 0;
            }
        }
        for (int i=1; i<=ord[0][0]; ++i)
        {
            int mini = INT_MAX;
            for (int j=0; j<N; ++j)
            {
                int sum = 0;
                for (int k=0; k<N; ++k)
                {
                    sum += abs(cnt[j][i]-cnt[k][i]);
                }
                if (mini > sum) mini = sum;
            }
            ret += mini;
        }
        if (flag == 0) cout << "Case #" << t << ": " << "Fegla Won" << endl;
        else cout << "Case #" << t << ": " << ret <<endl;
    }
}
