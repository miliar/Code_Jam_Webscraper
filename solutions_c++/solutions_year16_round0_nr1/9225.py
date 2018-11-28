#include <stdio.h>
#include<math.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int z=0;z<t;z++)
	{
		int arr[10];
		for(int i=0;i<10;i++)
			arr[i]=i;
		
		int n;
		scanf("%d",&n);
		
		int number=n;
		
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",z+1);
			continue;
		}
		int j=1;
		
		int flag=0;
		while(flag==0)
		{
			n=number*j;
			//calculate length
			int len=0;
			int x=n;
			while(x!=0)
			{
				len++;
				x=x/10;
			}
			
			//find digits
			for(int i=1;i<=len;i++)
			{
				int p=pow(10,i);		//printf("p is %d\n",p);
				int d=(n%p);			//printf("d is %d\n",d);
				p=pow(10,i-1);			//printf("p is %d\n",p);
				d=d/p;
				arr[d]=11;
				//printf("d is %d\n",d);
				//printf("%d ",d);
			}
			//check if all seen
			int i=0;
			while(arr[i]==11)
				i++;
			if(i==10)
			{
				flag=1;
				printf("Case #%d: %d\n",z+1,n);
			}
			j++;
		}
	}
	return 0;
}
