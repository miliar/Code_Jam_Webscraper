#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
//#include<conio.h>

#define MOD 1000000007

using namespace std;

int main()
{
int t,n,m,cur,flag1,flag2,flag;
int a[200][200];

scanf("%d",&t);

for(int i=1;i<=t;i++)
{
scanf("%d%d",&n,&m);

for(int j=0;j<n;j++)
{
for(int k=0;k<m;k++)
scanf("%d",&a[j][k]);
}

flag=0;

for(int j=0;j<n;j++)
{
	for(int k=0;k<m;k++)
	{
		
		flag1=0;
		flag2=0;
		cur=a[j][k];
	
		
		for(int x=0;x<m;x++) // seeing row wise
		{
			if(a[j][x]>cur)
            {
				flag1=1;
				break;
			}
		}
		
    	for(int x=0;x<n;x++)
			{
				if(a[x][k]>cur)
				{
					flag2=1;
					break;
				}
			}

		if(flag1==1&&flag2==1)
		{
			flag=1;
			break;
		}

	}

	if(flag==1)
	break;
}

if(flag==1)
printf("\nCase #%d: NO",i);

else
printf("\nCase #%d: YES",i);
}

//	getch();
	return 0;
}
