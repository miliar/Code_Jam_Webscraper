#include<stdio.h>
#include<algorithm>
using namespace std;
int a[10010];
int main()
{
	int T,t;
	freopen("A-large.in","r",stdin);
	freopen("output2.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		int n,c,i,ans=0;
		scanf("%d %d",&n,&c);
		for(i=1;i<=n;i++)scanf("%d",&a[i]);
		std::sort(a+1,a+n+1);
		int e=n;int s=1;
		while(s<=e){
			if(a[s]+a[e]<=c){
				s++;
				e--;
				ans++;
				continue;
			}
			e--;
			ans++;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}