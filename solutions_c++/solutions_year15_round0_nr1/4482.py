#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, c=1;
    cin >> t;

    while(t--)
    {
        int maxx;
        string s;

        cin >> maxx >> s;
        int ans = 0, curr = 0;
        int len = maxx+1;

        for(int i = 0; i < len; i++)
        {
            if(s[i] == '0')
                continue;
            if(curr < i)
            {
                ans += (i - curr);
                curr = i;
            }
            curr += (s[i] - '0');
            //cout << curr << " "<<i <<  endl;
        }
        cout <<"Case #"<< c <<": "<< ans << endl;
        c += 1;
    }
    return 0;
}
