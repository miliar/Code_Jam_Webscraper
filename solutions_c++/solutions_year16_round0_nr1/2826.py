#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

bool vis[10];
int n;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	
	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		scanf("%d", &n);
		if (n==0){
			printf("Case #%d: INSOMNIA\n", cs);
			continue;
		}

		memset(vis, 0, sizeof(vis));
		int x, remaining = 10;
		for (x = n; ; x += n){
			for(int y=x; y; y/=10){
				int z = y%10;
				if (!vis[z]){
					vis[z] = true;
					remaining--;
				}
			}

			if (remaining == 0) break;
		}
		
		printf("Case #%d: %d\n", cs, x);
	}	
	return 0;
}
