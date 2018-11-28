#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <ctime>
#include <cmath>
#include <algorithm>
using namespace std;
int T,x,y,sum,ans;
bool flag;
int a[5][5],b[5][5];
int t1[5],t2[5];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		scanf("%d",&x);
		for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
		scanf("%d",&a[i][j]);
		scanf("%d",&y);
		for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
		scanf("%d",&b[i][j]);
		for (int i=1;i<=4;i++)t1[i]=a[x][i];
		for (int i=1;i<=4;i++)t2[i]=b[y][i];
		sort(t1+1,t1+5);sort(t2+1,t2+5);
		sum=0;
		for (int i=1;i<=4;i++){
			flag=false;
			for (int j=1;j<=4;j++)
			if (t1[i]==t2[j])flag=true;
			if (flag)sum++,ans=t1[i];
		}
		if (sum==1)printf("%d\n",ans);
		else if (sum!=0)printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}
