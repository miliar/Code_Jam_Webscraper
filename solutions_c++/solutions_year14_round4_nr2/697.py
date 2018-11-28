#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int ans,n;
int a[1010],b[1010];

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int ca,cc=0;
	int i,j;
	int l,r,w;
	scanf("%d",&ca);
	while (ca--){
		scanf("%d",&n);
		for (i=0;i<n;i++) scanf("%d",&a[i]);
		for (i=0;i<n;i++) b[i]=a[i];
		sort(b,b+n);
		l=0;r=n-1;
		ans=0;
		for (i=0;i<n;i++){
			for (j=0;j<n;j++){
				if (b[i]==a[j]) {w=j;break;}
			}
			if (w-l<r-w){
				ans+=(w-l);
				for (j=w;j>l;j--) swap(a[j],a[j-1]);
				l++;
			}else{
				ans+=(r-w);
				for (j=w;j<n-1;j++) swap(a[j],a[j+1]);
				r--;
			}
		}
		printf("Case #%d: %d\n",++cc,ans);
	}
	return 0;
}
