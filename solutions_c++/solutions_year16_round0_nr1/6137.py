#include<stdio.h>

int main(){
	int t,track[10],count,r,j;
	long int n,i,tn;
	scanf("%d",&t);
	j=1;
	while(t--){
		scanf("%ld",&n);
		printf("Case #%d: ",j++);
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		for(i=0;i<10;i++)
			track[i]=0;
		count=0;
		
		i=n;
		while(1){
			tn=i;
			while(tn>0){
				r=tn%10;
				if(track[r]==0){
					track[r]=1;
					count++;
					if(count==10)
						break;
				}
				tn/=10;
			}
			if(count==10)
				break;
			i+=n;
		}
		
		printf("%ld\n",i);
			
	}
	return 0;
}
