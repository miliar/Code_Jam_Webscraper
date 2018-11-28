#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main()
{
	//freopen("result.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	int n;
	for(int i=0;i<cas;i++)
	{
		scanf("%d",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		char num[20],origin[20];
		for(int j=0;j<20;j++)
		{
			origin[j]='0';
			num[j]='0';
		}
		int digit=0;
		for(digit=0;;digit++)
		{
			if(n==0)
				break;
			num[digit]=n%10+'0';
			origin[digit]=n%10+'0';
			n/=10;
		}

		bool appear[10];
		for(int j=0;j<10;j++)
			appear[j]=false;
		
		for(int k=0;k<digit;k++)
			appear[num[k]-'0']=true;
		bool check=false;
		for(int j=0;j<=100;j++)
		{
			check=true;
			for(int k=0;k<10;k++)
				if(appear[k]==false)
				{
					check=false;
					break;
				}
			if(check==true)
				break;
			for(int k=0;k<digit;k++)
				num[k]+=(origin[k]-'0');
			
			int newdigit=0;
			for(int k=0;k<digit;k++)
			{
				if(num[k]>'9')
				{
					num[k]-=10;
					num[k+1]++;
					if(k+2>digit)
						newdigit=k+2;
					k--;
				}
			}
			if(newdigit!=0)
				digit=newdigit;
			for(int k=0;k<digit;k++)
				appear[num[k]-'0']=true;
		}
		printf("Case #%d: ",i+1);
		if(check==false)
			printf("INSOMNIA\n");
		else
		{
			for(int j=digit-1;j>=0;j--)
				printf("%c",num[j]);
			printf("\n");
		}
	}
	return 0;
}
