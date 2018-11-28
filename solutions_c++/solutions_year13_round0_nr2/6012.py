#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int N, n, m, a[105][105], cases = 0;
	scanf("%d", &N);
	while(N--){
        cases ++;
		int res = 0;
		scanf("%d%d", &n, &m);
		for(int i=1; i<= n; i++)
			for(int j=1; j<= m; j++) scanf("%d", &a[i][j]);
		for(int i=1; i<=n; i++)
			for(int j=1; j<=m; j++)
				if(a[i][j] == 1){
					int f = 0;
					for(int k=1; k<=m; k++)
						if(a[i][k] == 2) f = 1;
					if(!f)
						continue;
					f = 0;
					for(int k=1; k<=n; k++)
						if(a[k][j] == 2) f = 1;
					if(!f) continue;
					res = 1;
				}
		if(!res) printf("Case #%d: YES\n", cases);
		else printf("Case #%d: NO\n", cases);
	}
    return 0;
}
