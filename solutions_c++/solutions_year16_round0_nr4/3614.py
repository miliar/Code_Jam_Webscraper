#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int h=0; h<t; h++)
    {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << h+1 << ": ";
        if (k == 1)
        {
            cout << 1 << endl;
            continue;
        }
        if (c == 1)
        {
            if (s >= k)
                for (int i=0; i<k; i++)
                    cout << i+1 << " ";
            else
                cout << "IMPOSSIBLE";
            cout << endl;
            continue;
        }
        if (s >= k-1)
            for (int i=1; i<k; i++)
                cout << i+1 << " ";
            else
                cout << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
