#include<bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
//  freopen("t_case.txt","r",stdin);
    int t;
    cin>> t;
    repe(_case,1,t)
    {

        int q;
        cin >> q;
        string s;
        cin >> s;
        int count = (s[0] - '0');
        int req = 0;
        //dbg(count);
        int len = q + 1;
        rep(i, 1, len)
        {
            if(count < i)
                {
                    req += i - count;
                    count = i;

                }
            count += (s[i] - '0');
        }
        cout << "Case #" << _case <<": ";
        cout << req << "\n";
    }
    return 0;
}
