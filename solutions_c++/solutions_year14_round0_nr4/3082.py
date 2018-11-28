#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T;
int n;
double a[1005],b[1005];

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t=0;t<T;t++){
		printf("Case #%d: ",t+1);
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for (int i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int l=0,ans=0;
		for (int i=0;i<n;i++){
			while (a[l]<b[i]&&l<n) l++;
			if (l<n) ans++,l++;
		}
		printf("%d ",ans);
		ans=0; l=0;
		for (int i=0;i<n;i++){
			while (b[l]<a[i]&&l<n) l++;
			if (l<n) ans++,l++;
		}
		printf("%d\n",n-ans);
	}
	return 0;
}