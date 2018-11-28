#include "cstdio"
#include "math.h"
int main()
{
	freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,count=10;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int check[10] = {0};
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		for(int j=1;j;j++){
			int flag = 0;
			int temp = n*j;
			while(1==1){
				int tmp = temp/(int)pow(double(10),double(count--));
				if(tmp != 0){
					count+=2;
					break;
				}
			}
			for(int k=0;k<count;k++){
				check[temp%10] = 1;
				temp /= 10;
			}
			for(int k=0;k<10;k++){
				if(check[k] == 0){
					flag = 1;
					break;
				}
			}
			if(flag == 0){
				printf("Case #%d: %d\n", i+1,n*j);
				break;
			}
		}
	}
	return 0;
}