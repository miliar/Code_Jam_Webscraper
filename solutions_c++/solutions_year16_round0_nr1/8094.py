#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	int t,n;
	int arr[10];
	int temp,ans;

	scanf("%d",&t);
	for(int no = 1; no <= t; no++){
		scanf("%d",&n);
		memset(arr,0,sizeof(arr));				
		if(n == 0){
			printf("Case #%d: INSOMNIA\n",no);
			continue;
		}
		
		for(int i = 1;;i++){
			temp = n*i;		
			while(temp){
				//printf("%d ",temp%10);
				arr[temp%10]=1;
				temp = temp/10;
			}
			int j;
			for(j = 0; j < 10; j++)
				if(arr[j]==0)break;
			if(j == 10){
				ans = n*i;
				break;
			}
		}

		printf("Case #%d: %d\n",no,ans);
	}

}
