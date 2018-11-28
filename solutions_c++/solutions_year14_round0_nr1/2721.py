#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	freopen("A-small-attempt0 .in","r",stdin);
	freopen("ans","w",stdout);
	int t,count=1;
	scanf("%d",&t);
	while( t-- ) {
		int n,m,i,k,j;
		int a[5][5];
		
		scanf("%d",&n);
		int c=0;
		int b[4][4];
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++)
			scanf("%d",&a[i][j]);
			
		}
		scanf("%d",&m);
		
		for( i=0;i<4;i++) {
			for(j=0;j<4;j++)
			scanf("%d",&b[i][j]);
			
		}
	//		fclose(stdin);
			

		int ans;
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
			if(a[n-1][i]==b[m-1][j]) {
				c++;
				ans = a[n-1][i];
			}
			}
		}

		printf("Case #%d: ",count++);
		if(c==1)  {
			printf("%d\n",ans);
		}
		else if( c>1) {
			printf("Bad magician!\n");
		} else if( c==0) {
			printf("Volunteer cheated!\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

