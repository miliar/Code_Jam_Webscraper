#include <stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("inp.txt", "r", stdin);
	freopen("out3.txt","w",stdout);
	int t,l=1;
	scanf("%d",&t);
	while(t--){
		int n,i,j,x,war1 = 0,war2 = 0;
		scanf("%d",&n);
		double naomi[n],ken[n],c[n];
		for(i=0;i<n;i++){
			scanf("%lf",&naomi[i]);
		}
		for(i=0;i<n;i++){
			scanf("%lf",&ken[i]);
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		for(i=0;i<n;i++){
			c[i]=ken[i];
		}
		for(i=n-1;i>=0;i--){
			int flag=0;
			int m=-1;
			for(j=n-1;j>=0;j--){
				if(c[j]!=-1&&c[j]>naomi[i]){
					flag=1;
					m =j;
				}
				else if(c[j]!=-1){
					break;
				}
			}
			war2++;
			if(flag==1){
				c[m] = -1;
				war2--;
			}
			else{
				j = 0;
				while(j<n&&c[j]!=-1)
				j++;
				c[j]=-1;
			}
		}
		for(i=0,j=0;i<n&&j<n;i++){
			if(naomi[i]>ken[j]){
				war1++;
				j++;
			}
		}
		printf("Case #%d: %d %d\n",l,war1,war2);
		l++;
	}
	return 0;
}

