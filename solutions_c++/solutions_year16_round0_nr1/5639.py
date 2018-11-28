#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long t, x ;
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    cin >> t ;
    for (int i = 1 ; i <= t ; i++ )
    {
        cin >> x;
        long long N = x, c = 1;
        int mp[10] = {};
        if (x == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        while(true)
        {
            N = x * c;
            while(N > 0)
            {
                mp[N % 10] = 1;
                N /= 10;
            }
            int check = 1;
            for (int j = 0 ; j < 10 ; j++ )
            {
                if (!mp[j]) check = 0;
            }
            if (check)
            {
                cout << "Case #" << i << ": " << x * c<< endl;
                break;
            }
            c ++ ;
        }
    }
}
