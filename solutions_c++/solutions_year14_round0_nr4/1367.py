#include<stdio.h>
#include<algorithm>
using namespace std;

int n;
double a[1010]={0.0},b[1010]={0.0};
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,t2;
	int i,j,n;
	int ch=0,cnt=0,cnt2=0;
	scanf("%d",&t);
	for(t2=1;t2<=t;t2++){
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf",&a[i]);
		for(i=0;i<n;i++) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		if(b[n-1] == 1.0){
			ch=1;
		}
		for(i=0,j=ch;i<n;i++){
			while(j<n && b[i]>=a[j]) j++;
			if(j==n) break;
			cnt++, j++;
		}
		for(i=n-1,j=n-1;i>=0;i--){
			if(a[i]>=b[j]){
				cnt2++;
			}
			else j--;
		}
		printf("Case #%d: %d %d\n",t2,cnt,cnt2);
		cnt=cnt2=ch=0;
	}
	return 0;
}
