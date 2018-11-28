#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,u;
	scanf("%d",&t);
	u=t;
	while(t--){
		unsigned int temp, n;
		int i,flag;
		int num[10];
		scanf("%u",&n);
		temp=n;
		if(n==0){
			printf("Case #%d: INSOMNIA\n",u-t);
		}
		else{
			
			for(int j=0;j<10;j++)
				num[j]=0;
			i=1;
			while(1){
				flag=0;
				temp=i*n;
				while(temp){
					num[temp%10]=1;
					temp/=10;
					}
				for(int j=0;j<10;j++){
					if(num[j]!=1){
						flag=1;
						break;
					}
				}
				if(flag==0){
					printf("Case #%d: %u\n",u-t,i*n);
					break;
				}
				i++;
			}
		}
	}
	return 0;
}
