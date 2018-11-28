#include <bits/stdc++.h>
using namespace std;

int T;

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    int k, c, s;
    for(int t = 1;t <= T; ++t) {
        cin >> k >> c >> s;
        cout << "Case #" << t << ": ";
        if(s < k)
            cout << "IMPOSSSIBLE";
        else {
            for(int i = 1;i <= s; ++i)
                cout << i << ' ';
        }
        cout << '\n';
    }
    return 0;
}
