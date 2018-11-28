
#include <iostream>
#include <list>
#include <memory.h>

int arr[102];
char str[102];

int main(int argc, char** argv) {
	int i,j,k,cnt,transition;
	int test,T;
	freopen("C:\\Users\\raju\\Documents\\input.txt","r",stdin);
	freopen("C:\\Users\\raju\\Documents\\out.txt","w+",stdout);
	scanf("%d\n",&T);
	for(test=1;test<=T;test++)
	{
		
		memset(arr,0x00,sizeof(arr) );
		memset(str,0x00,sizeof(arr) );
		transition=0;
		cnt=0;
		scanf("%s\n",str);
		i=0;
		while(str[i] != 0)
		{
			if(str[i] == '+') arr[i] = 1;
			else if (str[i] == '-') arr[i] = 0;
			
			if(i >= 1 && str[i-1] != str[i])
			{
				transition++;
			}
			i++;
		}
		cnt = i;
		
		if(str[cnt -1] == '-') transition++; 
		printf("Case #%d: %d\n",test,transition);
	}//test
	return 0;
}

	
