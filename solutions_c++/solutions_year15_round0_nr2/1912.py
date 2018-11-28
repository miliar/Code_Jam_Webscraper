#include<stdio.h>
#include<string>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

int a[10000];
int n;

int main(){
	//freopen("stdin","r",stdin);
	//freopen("stdout","w",stdout);
	scanf("%d",&n);
	for (int time=0;time<n;time++)
	{
		int tot;
		int amax = 0;
		scanf("%d",&tot);
		for (int i=0;i<tot;i++){
			scanf("%d",a+i);
			amax = max(amax, a[i]);
		}
		int need = amax;
		for (int i=1;i<=amax;i++){
			int div = 0;
			for (int j=0;j<tot;j++)
				div += (a[j] / i) + ((a[j] % i)!=0) - 1;
			need = min(need, div + i);
		}
		printf("Case #%d: %d\n", time+1, need);
	}
	return 0;
}
