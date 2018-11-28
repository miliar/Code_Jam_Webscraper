#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inp2.in","r",stdin);
	int tc,lim,i,x,l,flag1,flag2,flag3,k,j,num,neg;
	char mstr[10009];
	int arr[5][5]={{0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
	scanf("%d",&tc);
	for(k=1;k<=tc;k++)
	{
		flag1=flag2=flag3=neg=0;
		scanf("%d%d",&l,&x);
		scanf("%s",mstr);
		lim=x*l;
		num=mstr[0]-'i'+2;
		if(num<0)
		{
			num=-num;
			if(neg==0)
				neg=1;
			else
				neg=0;
		}
		//printf("%d_",num);
		if(num==2&&flag1==0&&neg==0)
		{
			flag1=1;
			num=1;
		}
		
		for(i=1;i<lim;i++)
		{
			j=i%l;
			//printf("%d__",mstr[j]-'i'+2);
			num=arr[num][mstr[j]-'i'+2];
			if(num<0)
			{
				num=-num;
				if(neg==0)
					neg=1;
				else
					neg=0;
			}
			//printf("%d_",num);
			
			if(num==2&&flag1==0&&neg==0)
			{
				flag1=1;
				num=1;
			}
			else if(num==3&&flag1==1&&flag2==0&&neg==0)
			{
				flag2=1;
				num=1;
			}
			else if(num==4&&flag1==1&&flag2==1&&flag3==0&&neg==0)
			{
				flag3=1;
				i++;
				num=1;
				break;
			}
			
		}
		if(flag3==1)
		{
			num=1;
			for(;i<lim;i++)
			{
				j=i%l;
				num=arr[num][mstr[j]-'i'+2];
				if(num<0)
				{
					num=-num;
					if(neg==0)
						neg=1;
					else
						neg=0;
				}
			}
			if(num==1&&neg==0)
				printf("Case #%d: YES\n",k);
			else
				printf("Case #%d: NO\n",k);
		}
		else
			printf("Case #%d: NO\n",k);


	}
	return 0;
}