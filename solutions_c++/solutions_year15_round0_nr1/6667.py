#include<iostream>
using namespace std;
int main(){
	int t,n,i,a,x,j;
	int sum,invite;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	j=1;
	scanf("%d",&t);
	
	while(j<=t){
		scanf("%d",&n);
		sum=0;
		invite=0;
		for(i=0;i<=n;i++){
			
			scanf("%1d",&a);
			if(sum<i && a!=0){
				invite = invite + i-sum;
				sum= sum + invite;
			}
			sum+=a;
		}
		printf("Case #%d: %d\n",j,invite);
		j++;
	}
}
