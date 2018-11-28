#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("inp1.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    cin >> t;
    int tc = 1;
    while(t--)
    {
        int smx;
        string s;
        cin >> smx >> s;

        int ps = 0, ans = 0;
        for(int i = 0; i <= smx; i++)
        {
            if(s[i] != '0')
            {
                if(i <= ps)
                {
                    ps = ps + s[i] - '0';
                }
                else
                {
                    int temp = i - ps;
                    ans = ans + temp;
                    ps = i + s[i] - '0';
                }
            }
            //cout << i << " " << ps << " " << ans << endl;
        }
        cout << "Case #" << tc << ": " << ans << endl;
        tc++;
        //cout << ans << endl;
    }
}
