#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int T,N,M;

	int lawn[102][102];
	int rowMax[102],colMax[102];

	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		memset(lawn,0,sizeof(lawn));
		memset(rowMax,0,sizeof(rowMax));
		memset(colMax,0,sizeof(colMax));

		scanf("%d %d", &N, &M);
		for(int i=0;i<N;i++) 
			for(int j=0;j<M;j++) {
				int n;
				cin >> n;
				lawn[i][j]=n;
			}

		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++) {
				if(lawn[i][j] > rowMax[i]) rowMax[i] = lawn[i][j];
				if(lawn[i][j] > colMax[j]) colMax[j] = lawn[i][j];
			}

		int ok=1;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++) {
				int v = min(rowMax[i], colMax[j]);
				if(v!=lawn[i][j]) {
					ok=0;
					break;
				}
			}

			printf("Case \#%d: ", c);
			if(ok) printf("YES\n");
			else printf("NO\n");
	}

	return 0;
}