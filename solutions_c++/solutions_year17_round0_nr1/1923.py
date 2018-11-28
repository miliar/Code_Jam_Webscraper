#include <fstream>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <iomanip>
#include <queue>
#include <vector>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

typedef int INT;

#define int long long
#define double long double
int mod = 1e9+7;
int inf = 1e9;
vector<int> a;


INT main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int T;
    cin >> T;
    for (int t = 0; t<T; t++)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;
        bool ok = true;
        for (int i = 0; ok && i<s.size(); i++)
        {
            if (s[i]=='-')
            {
                ans++;
                if (i+k>s.size())
                {
                    ok = false;
                    continue;
                }
                for (int j = i; j<i+k; j++)
                {
                    if (s[j]=='+')
                        s[j] ='-';
                    else
                        s[j] = '+';
                }
            }
        }
        cout << "Case #" << t+1 <<": ";
        if (ok)
            cout << ans;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
