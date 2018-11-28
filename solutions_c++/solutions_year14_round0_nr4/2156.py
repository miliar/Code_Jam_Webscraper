#include<stdio.h>
#include<algorithm>
using namespace std;
double us[10000],aj[10000];
int main(){
	int t,count=1;
	scanf("%d",&t);
	while(t--){
		int n,i,j,k,x=0,y=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%lf",&us[i]);
		for(i=0;i<n;i++)scanf("%lf",&aj[i]);
		sort(us,us+n);
		reverse(us,us+n);
		sort(aj,aj+n);
		reverse(aj,aj+n);
		i=0,j=0,k=n-1;
		while(i<n){
			if(us[i]>aj[j]){
				y++;
				k--;
			}else{
				j++;
			}
			i++;
		}
		i=n-1;j=n-1;k=0;
		while(i>-1){
			if(us[i]>aj[j]){
				j--;
				x++;
			}else{
				if(us[i]>aj[k]){
					x++;
				}
				k++;
			}
			i--;
		}
		
		printf("Case #%d: %d %d\n",count++,x,y);
	}
	return 0;
}
