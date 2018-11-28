#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
const int mod = 1000000007;
typedef long long LL;

int a[5][5];
bool vis[20];

int main()
{
    int T, nc = 0;
    cin >> T;
    while(T--)
    {
        int n, m, ok = 0;
        printf("Case #%d: ", ++nc);
        memset(vis, 0, sizeof vis);

        cin >> n;
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++)
                cin >> a[i][j];
        }
        for(int i = 1; i <= 4; i++)
            vis[a[n][i]] = 1;

        cin >> n;
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++)
                cin >> a[i][j];
        }
        for(int i = 1; i <= 4; i++) {
            if(vis[a[n][i]]) {
                m = a[n][i];
                if(ok) ok = 2;
                else ok = 1;
            }
        }

        if(ok == 2) puts("Bad magician!");
        else if(ok == 0) puts("Volunteer cheated!");
        else cout << m << endl;
    }
}
