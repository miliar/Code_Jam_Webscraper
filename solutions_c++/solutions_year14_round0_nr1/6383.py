#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

const int N = 111;
int a[N][N],b[N][N];
int fir,sec;
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t,tt=0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&fir);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&sec);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
				scanf("%d",&b[i][j]);
		int count = 0,ans = 0;
		for(int i = 1;i <= 4;i++){
			for(int j = 1;j <= 4;j++){
				if(a[fir][i] == b[sec][j]){
					count++;
					ans = a[fir][i];
				}
			}
		}
		printf("Case #%d: ",++tt);
		if(count > 1) printf("Bad magician!\n");
		else if(count == 0) printf("Volunteer cheated!\n");
		else printf("%d\n",ans);
	}
	return 0;
}
