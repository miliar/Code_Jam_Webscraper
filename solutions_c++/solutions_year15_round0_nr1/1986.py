#include<stdio.h>
#include<string>
#include<queue>
#include<vector>
using namespace std;

int a[10000];
int n;

int main(){
	freopen("stdin","r",stdin);
	freopen("stdout","w",stdout);
	scanf("%d",&n);
	for (int i=0;i<n;i++)
	{
		int smax, tot, need;
		tot = 0; need = 0;
		scanf("%d", &smax);
		getchar();
		for (int j=0;j<=smax;j++){
			int d = getchar() - '0';
			if (tot<j){
				need += j - tot;
				tot = j;
			}
			tot += d;
		}
		printf("Case #%d: %d\n", i+1, need);
	}
	return 0;
}
