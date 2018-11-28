#include <bits/stdc++.h>
using namespace std;
#define maxn 1005
int main()
{
	//freopen("F:\\TestFiles\\B-large.in","r",stdin);
	//freopen("F:\\TestFiles\\B-large.out","w",stdout);
	int t;scanf("%d",&t);
	int testcase=1;
	while(t--){
		int n;scanf("%d",&n);
		int a[maxn];
		int maxx=0;
		for (int i=0;i<n;i++){
			scanf("%d",&a[i]);
			maxx=max(maxx,a[i]);
		}
		int ans=maxx;
		for (int i=maxx-1;i>=1;i--){
			int sum=i;
			for (int j=0;j<n;j++){
				if (a[j]%i==0) sum+=(a[j]/i-1);
				else sum+=(a[j]/i);
			}
			ans=min(ans,sum);
		}
		printf("Case #%d: %d\n",testcase++,ans);
	}
	return 0;
}