#include<stdio.h>
int bin_search(int num,int low,int high)
{
	int mid=(low+high)/2;
	int sq=mid*mid;
	if(low<=high)
	{
		if(sq==num)
			return mid;
		else if(num<sq)
			return bin_search(num,low,mid-1);
		else
			return bin_search(num,mid+1,high);
	}
	else
		return -1;
}
int main()
{
	int lowp=1,highp=32,i,j,t,num,reverse,sq,count,a,b;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		count=0;
		scanf("%d%d",&a,&b);
		for(j=a;j<=b;j++)
		{
			reverse=0;
			num=j;
			while(num>0)
			{
				reverse=(reverse*10)+num%10;
				num/=10;
			}
			if(reverse==j)
			{
				sq=bin_search(j,lowp,highp);	
				if(sq!=-1)
				{
					reverse=0;
					num=sq;
					while(num>0)
					{
						reverse=(reverse*10)+(num%10);
						num/=10;
					}
					if(reverse==sq)
						count++;			
				}
			}
		}
		printf("Case #%d: %d\n",i+1,count);
	}
}
