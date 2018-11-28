#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
int sine=1;
char mul(char a, char b)
{
	char ans;
	if(a=='1')
	{
		ans=b;
	}	
	else if(a=='i')
	{
		if(b=='1')
		{
			ans='i';
		}
		else if(b=='i')
		{
			sine=-1;
			ans='1';
		}	
		else if(b=='j')
		{
			ans='k';
		}
		else
		{
			sine=-1;
			ans='j';
		}
	}	
	else if(a=='j')
	{
		if(b=='1')
		{
			ans='j';
		}
		else if(b=='i')
		{
			sine=-1;
			ans='k';
		}	
		else if(b=='j')
		{
			sine=-1;
			ans='1';
		}
		else
		{
			ans='i';
		}
	}	
	else 
	{
		if(b=='1')
		{
			ans='k';
		}
		else if(b=='i')
		{
			ans='j';
		}	
		else if(b=='j')
		{
			sine=-1;
			ans='i';
		}
		else
		{
			sine=-1;
			ans='1';
		}
	}
	return ans;	
}
int main()
{
	int t,l,i,j,k,len,pr_sin,count,seq=0;
	long long x;
	scanf("%d",&t);
	while(t--)
	{
		seq++;
		int sign[10005];
		char pro[10005],str[10005],product;
		scanf("%d %lld",&l,&x);
		scanf("%s",str);
		printf("Case #%d: ",seq);
		pro[0]=str[0];
		sign[0]=1;
		for(i=1;str[i]!='\0';i++)
		{
			sine=1;
			pro[i]=mul(pro[i-1],str[i]);
			sign[i]=sign[i-1]*sine;
		}
		len=i;
		if(x%4==0)
		{
			printf("NO\n");
			continue;
		}
		if(x%4==1)
		{
			if (sign[len-1]!=-1 || pro[len-1]!='1')
			{
				printf("NO\n");
				continue;
			}
		}
		else if(x%4==2)
		{
			if(pro[len-1]=='1' )
			{
				printf("NO\n");
				continue;
			}
		}
		else if(x%4==3)
		{
			if(pro[len-1]!='1' || sign[len-1]!=-1)
			{
				printf("NO\n");
				continue;
			}
		}
		count=0;
		product='1';
		pr_sin=1;
		for(k=1;k<=min(x,(long long)10);k++)
		{
			for(i=0;i<len;i++)
			{
				sine=1;
				product=mul(product,str[i]);
				pr_sin=pr_sin*sine;
				if(count==0 && product=='i' && pr_sin==1)
					count++;
				if(count==1 && product=='k' && pr_sin==1)
				{
					count++;
					printf("YES\n");
					break;
				}	
			//	printf("%c %d\n",product,pr_sin);		
			}
			if(count==2)
				break;
			if(k==min(x,(long long)10))
				printf("NO\n");
		}
	}
	return 0;
}
