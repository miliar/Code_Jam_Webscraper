#include <bits/stdc++.h>

using namespace std;

int main(int argc,char *argv[])
{
    int T;
    cin >> T;
    for (int t=0;t<T;t++)
    {
        int X;
        cin >> X;
        char buf[65536];
        cin.getline(buf, 65536);
        string s = buf;
        int ans = 0;
        int cnt = 0;
        for (int i=0;i<=X;i++)
        {
            int v = s[i+1]-'0';
            if (cnt>=i)
            {
                cnt += v;
            } else if (v>0)
            {
                ans += i-cnt;
                cnt = i+v;
            }
        }
        cout << "Case #" << t+1 << ": " << ans << endl;
    }

  return 0;
}
