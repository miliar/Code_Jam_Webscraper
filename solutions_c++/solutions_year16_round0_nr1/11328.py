#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn=100000;
bool vis[15];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T, n;
	cin >> T;
	int kase=0;
	while (T--) {
		cin >> n;
		for (int i=0; i<=0; i++) {
            int cnt=0;
            memset(vis, 0, sizeof(vis));
            int j;
            for (j=1; j<maxn; j++) {
                int temp=n*j;
                while (temp) {
                    int d=temp%10;
                    if (!vis[d]) {
                        vis[d]=1; cnt++;
                    }
                    temp/=10;
                }
                if (cnt==10) break;
            }
            printf("Case #%d: ", ++kase);
            if (cnt==10) printf("%d\n", j*n);
            else puts("INSOMNIA");
        }
	}
}
