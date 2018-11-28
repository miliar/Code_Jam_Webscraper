#include<stdio.h>

int sepratenum(int num)
{
	if(num<10){
	    return num;
	}
	else{
	    return num%10;
	}
}

int main()
{
    int test,i,j,n,m,count,p;

    scanf("%d",&test);

	for(i=0;i<test;i++)
	{
		scanf("%d",&n);
		if(n==0)
		{
	 	printf("Case #%d: INSOMNIA\n",i+1);
	 	continue;
	   }
	
        int arr[10]={0};
		int j=1;
		int count=1;

		while(count < 11)
 		{
 			m=n*j++;
 			while(m!=0)
			{
				p=sepratenum(m);
				if(arr[p]==0)
				{
					arr[p]=count++;
				}
 				m=m/10;
			}
		}
		m=n*(--j);
		printf("Case #%d: %d\n",i+1,m);
	}	
}
