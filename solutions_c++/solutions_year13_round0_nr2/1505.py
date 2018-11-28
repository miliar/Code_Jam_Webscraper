#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<algorithm>

using namespace std;

#define NAME "B-large"

int T, n, m, yes;
int a[200][200];

int main(){
	freopen(NAME".in", "r", stdin);
	freopen(NAME".out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d%d", &n, &m);
		for(int i = 0; i <= max(n, m); i++){
			a[i][0] = 0;
			a[0][i] = 0;	
		}	
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= m; j++){
				scanf("%d", &a[i][j]);
				if (a[i][j] > a[i][0]) 
					a[i][0] = a[i][j];
				if (a[i][j] > a[0][j]) 
					a[0][j] = a[i][j];
			}
		}
		yes = 1;
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= m; j++){
		    	if (a[i][j] < a[i][0] && a[i][j] < a[0][j]){
		    		yes = 0;
		    		break;
		    	}
		    }
		    if (yes == 0)  
		    	break;
		}
		printf("Case #%d: ", t);
		if (yes) 
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}