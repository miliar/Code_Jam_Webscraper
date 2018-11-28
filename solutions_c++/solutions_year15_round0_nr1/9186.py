#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("output.out", "w", stdout);
    int N, Sh, ans, cur, sz;
    string S;
    scanf("%d", &N);
    for(int i = 0; i < N; ++i)
    {
        scanf("%d", &Sh);
        cin >> S;
        ans ^= ans;
        cur ^= cur;
        sz = S.size();
        for (int j = 0; j < sz; ++j)
        {
            if(cur + ans < j) {
                ans = j - cur;
            }
            cur += (S[j] - '0');
        }
        printf("Case #%d: %d\n",i+1, ans);
    }
    return 0;
}
