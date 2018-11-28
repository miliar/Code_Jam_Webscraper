#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int T,x,y,a[10][10],b[10][10];
int main(){
	scanf("%d",&T);
	for(int tt=1;tt<=T;++tt){
		printf("Case #%d: ",tt);
		scanf("%d",&x);
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				scanf("%d",&a[i][j]);
		scanf("%d",&y);
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				scanf("%d",&b[i][j]);
		int sum=0,ans=0;;
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				if(a[x][i]==b[y][j])	ans=a[x][i],sum++;
		if(sum==1)	printf("%d\n",ans);
		else if(sum>1)	printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}	
	return 0;
}
