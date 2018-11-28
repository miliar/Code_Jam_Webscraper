#include<stdio.h>

int main()
{
int t,n,m,cur,i,j,k,x,flag1,flag2,flag;
int a[200][200];
freopen("input.txt","r",stdin);
freopen("out.txt","w",stdout);

scanf("%d",&t);

for(i=1;i<=t;i++)
{
scanf("%d%d",&n,&m);

for(j=0;j<n;j++)
{
for(k=0;k<m;k++)
scanf("%d",&a[j][k]);
}

flag=0;

for(j=0;j<n;j++)
{
    for(k=0;k<m;k++)
	{
		
		flag1=0;
		flag2=0;
		cur=a[j][k];
	
		
		for(x=0;x<m;x++) // seeing row wise
		{
			if(a[j][x]>cur)
            {
				flag1=1;
				break;
			}
		}
		
    	for(x=0;x<n;x++)    //column wise
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
printf("Case #%d: NO\n",i);

else
printf("Case #%d: YES\n",i);
}

	return 0;
}

