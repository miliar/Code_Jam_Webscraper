#include<iostream>
#include<cstdio>
using namespace std;
int t,a[4][4],b[4][4],r1,r2;
int main(){
	freopen("1.in","r",stdin);
	scanf("%d",&t);
	for(int c = 1; c <= t; c++){
		scanf("%d",&r1);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j<4; j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&r2);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j<4; j++)
				scanf("%d",&b[i][j]);
		r1--;r2--;
		int num = 0, count = 0;
		for(int j1 = 0; j1 < 4;j1++)
			for(int j2 = 0; j2 < 4; j2++){
				if(a[r1][j1]==b[r2][j2]){
					num=a[r1][j1];
					count++;
				}
			}
		if(count==0) printf("Case #%d: Volunteer cheated!\n",c);
			else if(count==1) printf("Case #%d: %d\n",c,num);
			else printf("Case #%d: Bad magician!\n",c);
	}
	fclose(stdin);
	return 0;
}
