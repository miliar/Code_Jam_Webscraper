#include <bits/stdc++.h>

using namespace std;

int ar[20][20],used[20],a,n;

int main() {
	freopen("1.out","w",stdout);
	scanf("%d",&n);
	
	for(int i=1;i<=n;i++) {
		memset( used , 0 , sizeof used );
		scanf("%d",&a);
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
				scanf("%d",&ar[j][k]);
		
		for(int j=1;j<=4;j++)
			used[ ar[a][j] ] = 1;
			
		scanf("%d",&a);
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
				scanf("%d",&ar[j][k]);
				
		int t = 0 , r;
		for(int j=1;j<=4;j++) {
			if( used[ ar[a][j] ] ) t++ , r = ar[a][j];
		}
		printf("Case #%d: ",i);
		if( !t ) printf("Volunteer cheated!\n");
		else if( t == 1 ) printf("%d\n",r);
		else printf("Bad magician!\n");
	}
	
	
	
	return 0;
}
