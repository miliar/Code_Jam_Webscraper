#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;
typedef long long ll;
typedef pair<int,int> pii;
#define MP make_pair
#define A first
#define B second

void solve()
{
    int N, X; cin >> N >> X;
    vector<int> A(N); for (int i=0; i<N; i++) cin >> A[i];
    sort(A.begin(), A.end(), greater<int>());
    vector<bool> bad(N);
    int ans = 0;
    for (int i=0; i<N; i++)
    {
        if (bad[i]) continue;
        bad[i] = true;
        ans++;
        for (int j=i+1; j<N; j++)
        {
            if (bad[j]) continue;
            if (A[i]+A[j] <= X)
            {
                bad[j] = true;
                break;
            }
        }
    }
    cout << ans << '\n';
}

int main()
{
    int t; cin >> t;
    for (int kase=1; kase<=t; kase++)
    {
        cout << "Case #" << kase << ": ";
        solve();
    }
    return 0;
}
