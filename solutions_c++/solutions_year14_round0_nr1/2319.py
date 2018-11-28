#include <iostream>
#include <cstdio>
using namespace std;

int t;
int a[10][10];
int b[10][10];

int main(){
	scanf("%d",&t);
	for(int tt=1; tt<=t; tt++){
		int a1,a2;
		scanf("%d",&a1);
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++)
				scanf("%d",&a[i][j]);
		}
		scanf("%d",&a2);
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++)
				scanf("%d",&b[i][j]);
		}
		int cnt=0,ans;
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++){
				if(a[a1][i] == b[a2][j]){
					cnt++;
					ans=a[a1][i];
				}
			}
		}
		if(cnt== 0)
			printf("Case #%d: Volunteer cheated!\n",tt);
		if(cnt == 1)
			printf("Case #%d: %d\n",tt,ans);
		if(cnt > 1) printf("Case #%d: Bad magician!\n",tt);
	}
	return 0;
}
