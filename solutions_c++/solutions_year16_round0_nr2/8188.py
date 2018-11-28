#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	int t;
	char arr[110];

	int len,ans;

	scanf("%d",&t);
	for(int no = 1; no <= t; no++){
		scanf("%s",arr);
		
		len = strlen(arr);
		int temp = 0;
		ans = 0;
		if(arr[0] == '-') ans = 1;
		else if(arr[0] == '+') temp = 1;
		for(int i = 1; i < len; i++){
			if(arr[i]=='+') temp = 1;			
			else if(arr[i] == '-' && arr[i-1] != '-'){
				ans += temp+1; 
			}
		}
		printf("Case #%d: %d\n",no,ans);
	}
	return 0;
}

