#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>

using namespace std;

int a[1010];
int l[1010],r[1010];
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,n,ri=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		memset(l,0,sizeof(l));
		memset(r,0,sizeof(r));
		for(int i=0;i<n;i++){
			for(int j=0;j<i;j++)
				if(a[j]>a[i])l[i]++;
			for(int j=i+1;j<n;j++)
				if(a[j]>a[i])r[i]++;

		}
		int ans=0;
		for(int i=0;i<n;i++){
			ans+=min(l[i],r[i]);
		}

		printf("Case #%d: %d\n",ri++,ans);
	}

	return 0;
}
