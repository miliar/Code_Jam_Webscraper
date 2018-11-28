
#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,u;
	scanf("%d",&t);
	u=t;
	while(t--){
		int i,n;
		char num[101];
		scanf("%s",num);
		i=0;
		int count=0;
		char flag=num[0];
		n=strlen(num);
		while(i<n){
			if(num[i]!=flag){
				flag=num[i];
				count++;
			}
			i++;
		}
		if(num[i-1]=='-'){
			count++;
		}
		printf("Case #%d: %d\n",u-t,count);
		
	}
	return 0;
}
