#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MOD 1000000007

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T; string S;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        cin >> S;
        int N = S.length();
        reverse(S.begin(),S.end());
        int C = 0;
        for(int i = 0; i < N; i++)
        {
            if(S[i] == '+' && C%2 == 1) C++;
            else if(S[i] == '-' && C%2 == 0) C++;
        }
        printf("Case #%d: %d\n",t,C);
    }
    #ifndef ONLINE_JUDGE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
