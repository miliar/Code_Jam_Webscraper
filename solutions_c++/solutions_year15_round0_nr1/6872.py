#include <stdio.h>
#include<string>

typedef long long lld;

int T,K=0;

lld Smax,k=0,sum,need,need_sum;
char str[2000];


int main()
{
	
	freopen("input_large.in","r",stdin);
	freopen("output.txt","w",stdout);
	for (scanf("%d",&T);T--;){
		scanf("%lld%s",&Smax,str);
	//	int S=0;
	//	scanf("%d %s",&S,str);
		
		sum=0;
		sum+=str[0]-48;
		need_sum=0;
		for(int i=1;i<strlen(str);i++){
			if(sum>=i){
				sum+=str[i]-48;
			//	printf("sum=%lld ",sum);
			}
			else{
	//			printf("sum=%lld, i=%d, need=%lld str[%d]=%c\n",sum,i,need,i,str[i]);
				need=i-sum;
				sum+=need;
				sum+=str[i]-48;
				need_sum+=need;
				
			}
		}

	//	printf("T=%d %lld, strlen=%d \t",T,Smax,strlen(str));
		printf("Case #%d: %lld\n",++K,need_sum);

	}
}