#include<iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for(int t = 0;t < T;t ++)
    {
        int k;
        cin >> k;
        string s;
        cin >> s;
        int cnt = 0 , ans = 0;
        for(int i = 0;i <= k;i ++)
        {
            if(s[i] != '0')
                ans += max(0 , i - cnt) , cnt = max(cnt , i);
            cnt += (int)s[i] - (int)'0';
            //cout << ans << " " << cnt << endl;
        }
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
    return 0;
}
