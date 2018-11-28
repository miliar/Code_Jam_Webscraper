#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    string S;
    int T, cas = 1;
    cin >> T;
    while (T--)
    {
        int n;
        scanf ("%d", &n);
        cin >> S;
        int N = S.size();
        long long ans = 0, cnt = 0;
        for (int i = 0; i < N; i++)
        {
            if (S[i]>'0')
            {
                ans += max((long long)0, (long long)i-cnt);
                cnt += max((long long)0, (long long)i-cnt) + S[i]-'0';

            }
        }
        printf("Case #%d: ", cas++);
        cout << ans << endl;
    }
    return 0;
}
