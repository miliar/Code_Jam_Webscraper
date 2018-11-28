#include <bits/stdc++.h>

using namespace std;

int main(int argc,char *argv[])
{
    char buf[65536];
    int T;
    cin >> T;
    cin.getline(buf, 65536);
    for (int t=0;t<T;t++)
    {
        cin.getline(buf, 65536);
        string s = buf;
        int n = s.length();
        vector<char> dt;
        for (int i=0;i<n;i++)
            dt.push_back(s[i]);

        int cnt = 0;
        for (int i=n-1;i>=0;i--)
        {
            if (dt[i]=='+') continue;
            if (dt[0]=='+')
            {
                for (int k=0;k<i;k++)
                    if (dt[k]=='+')
                        dt[k] = '-';
                    else break;
                cnt++;
            }
            reverse(dt.begin(), dt.begin()+i+1);
            for (int j=0;j<=i;j++)
                if (dt[j]=='+')
                    dt[j] = '-';
                else
                    dt[j] = '+';
            cnt++;
        }

        dt.resize(0);
        for (int i=0;i<n;i++)
            dt.push_back(s[i]);
        int cnt2 = 1;
        for (int i=n-1;i>=0;i--)
        {
            if (dt[i]=='-') continue;
            if (dt[0]=='-')
            {
                for (int k=0;k<i;k++)
                    if (dt[k]=='-')
                        dt[k] = '+';
                    else break;
                cnt2++;
            }
            reverse(dt.begin(), dt.begin()+i+1);
            for (int j=0;j<=i;j++)
                if (dt[j]=='+')
                    dt[j] = '-';
                else
                    dt[j] = '+';
            cnt2++;
        }
        cnt = min(cnt, cnt2);

        cout << "Case #" << t+1 << ": " << cnt << endl;
    }
    return 0;
}
