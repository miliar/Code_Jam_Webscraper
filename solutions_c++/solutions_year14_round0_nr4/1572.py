#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int test,N,ans1,ans2;
double a[1005],b[1005];
int main(){
	freopen("i.txt","r",stdin);
	scanf("%d",&test);
	for (int testcase=1;test--;testcase++){
		printf("Case #%d: ",testcase);
		scanf("%d",&N);
		for (int i=1;i<=N;i++) scanf("%lf",&a[i]);
		for (int i=1;i<=N;i++) scanf("%lf",&b[i]);
		sort(a+1,a+N+1);
		sort(b+1,b+N+1);
		ans1=N;
		int i,j;
		i=1;
		j=1;
		for (;j<=N;j++){
			if (a[j]<b[i])
				ans1--;
			else
				i++;
		}
		ans2=0;
		i=1;
		j=1;
		for (;j<=N;j++){
			if (b[j]<a[i]) 
				ans2++;
			else
				i++;
		}
		printf("%d %d\n",ans1,ans2);
	}
	return 0;
}
