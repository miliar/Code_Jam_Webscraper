#include <cstdio>
#include <memory.h>
#include <algorithm>

using namespace std;

int a[102][102];
int h[102], w[102];

int main(){ //freopen("in.txt", "r", stdin);
		//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);

	for(int r=1; r<=T; r++){
		int n, m;
		scanf("%d %d", &n, &m);
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				scanf("%d", &a[i][j]);

		printf("Case #%d: ", r); 

		bool ans = 1;
		
		memset(h, 0, sizeof(h));
		memset(w, 0, sizeof(w));

		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				w[i] = max( w[i], a[i][j] );
				h[j] = max( h[j], a[i][j] );
			}
		}
		

		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				bool ch = 0;
				if( w[i] <= a[i][j] )
					ch = 1;
				if( h[j] <= a[i][j] )
					ch = 1;
				if( ch == 0 )
					ans = 0;
			}
		}

		if( ans ) puts("YES");
		else puts("NO");
	}
}