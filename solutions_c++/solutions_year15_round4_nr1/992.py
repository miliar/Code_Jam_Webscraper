#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <iomanip>
#include <string>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>

#define X first
#define Y second
#define mp make_pair
#define pb push_back

typedef long long ll;

using namespace std;

char s[110][110];
int c[110][110], n, m;
bool posl[110][110], posr[110][110], posd[110][110], posu[110][110];
void solve() {
    cin>>n>>m;
    for (int i = 0; i < n; i++) {
        cin>>s[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            posl[i][j] = posr[i][j] = posd[i][j] = posu[i][j] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        int j = 0;
        while (s[i][j] == '.' && j < m) j++;
        if (j == m) continue;
        posl[i][j] = 0;
    }
    for (int i = 0; i < n; i++) {
        int j = m - 1;
        while (s[i][j] == '.' && j >= 0) j--;
        if (j < 0) continue;
        posr[i][j] = 0;
    }
    for (int j = 0; j < m; j++) {
        int i = 0;
        while (s[i][j] == '.' && i < n) i++;
        if (i == n) continue;
        posu[i][j] = 0;
    }
    for (int j = 0; j < m; j++) {
        int i = n - 1;
        while (s[i][j] == '.' && i >= 0) i--;
        if (i < 0) continue;
        posd[i][j] = 0;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (s[i][j] == '.') {
                continue;
            }
            //cerr<<posl[i][j]<<" "<<posr[i][j]<<" "<<posu[i][j]<<" "<<posd[i][j]<<endl;
            if (posl[i][j] == 0 && posr[i][j] == 0 && posd[i][j] == 0 && posu[i][j] == 0) {
                cout<<"IMPOSSIBLE"<<endl;
                return ;
            }
            ans += (s[i][j] == '<' && posl[i][j] == 0);
            ans += (s[i][j] == '>' && posr[i][j] == 0);
            ans += (s[i][j] == 'v' && posd[i][j] == 0);
            ans += (s[i][j] == '^' && posu[i][j] == 0);
        }
    }
    cout<<ans<<endl;
}

int main() {
    freopen("Asm.txt", "r", stdin);
    freopen("Asm.out", "w", stdout);
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        printf("Case #%d: ", i );
        solve();
    }
	return 0;
}
