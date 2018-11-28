#include<stdio.h>
#include<string.h>

int num[10];

int main(){
	int T;
	freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	scanf("%d",&T);
	for(int q=1;q<=T;++q){
		int n;
		scanf("%d",&n);
		printf("Case #%d: ",q);
		if(n==0){
			printf("INSOMNIA\n");
		}
		else{
			memset(num,0,sizeof(num));
			for(int i=1;i<=80;++i){
				int tmp=i*n;
				while(tmp){
					int b=tmp%10;
					tmp/=10;
					num[b]=1;
				}
				if(num[0]&&num[1]&&num[2]&&num[3]&&num[4]&&num[5]&&num[6]&&num[7]&&num[8]&&num[9]){
					printf("%d\n",i*n);
					break;	
				}
			}
		}
	}
	return 0;
}
