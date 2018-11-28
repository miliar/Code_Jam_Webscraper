#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int N, M, a[111][111];
int H[111], V[111];

bool solve()
{
    memset(H, 0, sizeof(H));
    memset(V, 0, sizeof(V));
    for(int i = 0; i < N; i++) for(int j = 0; j < M; j++)
    {
        H[i] = max(H[i], a[i][j]);
        V[j] = max(V[j], a[i][j]);
    }
    for(int i = 0; i < N; i++) for(int j = 0; j < M; j++)
    {
        if(H[i] > a[i][j] and V[j] > a[i][j]) return 0;
    }
    return 1;
}

int main()
{
    freopen("Blarge.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    int T = 0;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N >> M;
        for(int i = 0; i < N; i++) for(int j = 0; j < M; j++) cin >> a[i][j];
        cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << endl;
    }
}
