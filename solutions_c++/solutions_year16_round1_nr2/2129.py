#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int num[3000];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int T, n;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++) {
		memset(num, 0, sizeof(num));
        printf("Case #%d:",cas);
        scanf("%d",&n);
        for(int i = 1; i < 2*n; i++) {
			for(int j = 0; j < n; j++) {
					int x;
				scanf("%d",&x);
				num[x]++;
			}
        }
        for(int i = 0; i <= 2500; i++) if(num[i]&1) printf(" %d",i);
        puts("");
	}
    return 0;
}
