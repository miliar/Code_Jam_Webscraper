#include <bits/stdc++.h>

using namespace std;

const int maxN = 1e3+10;
int test,N,K,ans;
string S;

int main()
{
    freopen("googlejam.inp","r",stdin);
    freopen("googlejam.out","w",stdout);
    cin >> test;
    for (int t=1; t <= test; t++)
    {
        cout << "Case #" << t << ": ";
        cin >> S >> K;
        N = S.size(); ans = 0;
        for (int i=0; i <= N-K; i++)
            if (S[i] == '-')
            {
                ans++;
                for (int j=i; j < i+K; j++)
                    S[j] = (S[j] == '-') ? '+' : '-';
            }
        bool flag = 1;
        for (int i=0; i < N; i++)
            if (S[i] == '-') flag = 0;
        if (flag) cout << ans << endl;
        else puts("IMPOSSIBLE");
    }
}
