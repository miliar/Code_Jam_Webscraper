
#include <iostream>
#include <list>
#include <memory.h>

char arr[1002];
char outarr[2002];
int main(int argc, char** argv) {
	int i,j,k,cnt1,cnt2,transition;
	int test,T;
	freopen("C:\\Users\\raju\\Documents\\input.in","r",stdin);
	freopen("C:\\Users\\raju\\Documents\\out.txt","w+",stdout);
	scanf("%d\n",&T);
	for(test=1;test<=T;test++)
	{
		
		memset(arr,0x00,sizeof(arr) );
		memset(outarr,0x00,sizeof(outarr));
		transition =1000;
			scanf("%s",arr);
		outarr[transition]=arr[0];
		cnt1 = transition -1;
		cnt2 = transition +1;
	
		for(i=1;arr[i];i++)
		{
			if(arr[i] >= outarr[transition])
			{
				outarr[cnt1] = arr[i];
				transition =cnt1;
				cnt1--;
			}
			else{
				outarr[cnt2]=arr[i];
				cnt2++;
			}
		}
		printf("Case #%d: ",test);
		for(i=transition;i <cnt2;i++)
		{
			printf("%c",outarr[i]);	
		}
		printf("\n");
	}//test
	return 0;
}

	
