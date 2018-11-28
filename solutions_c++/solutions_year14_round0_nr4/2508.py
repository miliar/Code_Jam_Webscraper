#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <ctime>
using namespace std;
double a[1010],b[1010];
bool use[1010];
bool flag;
int T,N,ans1,ans2;
int main(){
	//freopen("D.in","r",stdin);
	//freopen("D.out","w",stdout);
	scanf("%d",&T);
	int tt=0;
	while (T--){
		tt++;
		printf("Case #%d: ",tt);
		scanf("%d",&N);
		for (int i=1;i<=N;i++)scanf("%lf",&a[i]);
		for (int i=1;i<=N;i++)scanf("%lf",&b[i]);
		sort(a+1,a+N+1);sort(b+1,b+N+1);
		int l1=1,r1=N;
		ans1=ans2=0;
		for (int i=N;i;i--){
			if (a[i]>b[r1]){
				ans2++;l1++;
			}else r1--;
		}
		memset(use,true,sizeof(use));
		for (int i=N;i;i--){
			flag=true;
			for (int j=N;j;j--)
			if (use[j]&&a[i]>b[j]){
				use[j]=false;
				ans1++;
				flag=false;
				break;
			}
			if (flag){
				for (int j=N;j;j--)
				if (use[j]){use[j]=false;break;}
			}
		}
		printf("%d %d\n",ans1,ans2);
	}
}
