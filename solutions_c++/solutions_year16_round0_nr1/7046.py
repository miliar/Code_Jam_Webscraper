#include<stdio.h>
int main(){
	int t;
	int cnt=1;
	 freopen("A-large.in","r",stdin);
     freopen("out.in","w",stdout);
     scanf("%d",&t);
	while(t--){
		int n;
		bool use[10]={false};
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: ",cnt++);
			printf("INSOMNIA\n");
			continue;
		}
		int res=0;
		long long int sum=n;
		for(int i=1;sum>=0;i++){
			sum=n*i;
			long long int l=sum;
			while(l!=0){
			long long int d=l%10;
				if(use[d]==false){
					use[d]=true;
					res++;
				}
				if(res==10){
					break;
				}
				l/=10;
			}
			if(res==10){
				break;
			}
		}
		printf("Case #%d: ",cnt++);
		printf("%I64d\n",sum);
	}
}
