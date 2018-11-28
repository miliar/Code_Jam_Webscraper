#include <stdio.h>
#include <math.h>
int tcase,n,m,a[10011][10011],table[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
char str[10011];
int main()
{
	int i,j,loop,temp,val;
	bool flag;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&tcase);
	for(loop=1;loop<=tcase;loop++)
	{
		flag=false;
		scanf("%d %d",&n,&m);
		scanf("%s",str);
		for(i=0;i<n;i++)
		{
			if(str[i]=='1')
				str[i]=1;
			else if(str[i]=='i')
				str[i]=2;
			else if(str[i]=='j')
				str[i]=3;
			else if(str[i]=='k')
				str[i]=4;
		}
		for(i=1;i<m;i++)
		{
			for(j=0;j<n;j++)
				str[i*n+j]=str[j];
		}
		n*=m;
		for(i=0;i<n;i++)
		{
			val=str[i];
			a[i][i]=val;
			for(j=i+1;j<n;j++)
			{
				temp=1;
				if(val<0) temp*=(-1);
				val=table[abs(val)][str[j]]*temp;
				a[i][j]=val;
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n-1;j++)
			{
				if(a[0][i]==2 && a[i+1][j]==3 && a[j+1][n-1]==4)
				{
					flag=true;
					break;
				}
			}
			if(flag) break;
		}
		if(flag==true)
			printf("Case #%d: YES\n",loop);
		else
			printf("Case #%d: NO\n",loop);
	}
	return 0;
}