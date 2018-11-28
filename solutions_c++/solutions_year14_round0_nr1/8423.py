#include <iostream>
using namespace std;

int main() 
{
	int t,r=1;
	scanf("%d",&t);
	while(r<=t)
	{
	int cnt,pos,a,b,i,j,x[5][5],y[5][5];
	scanf("%d",&a);
	for(i=0;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
			scanf("%d",&x[i][j]);
		}
	}
	scanf("%d",&b);
	for(i=0;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
			scanf("%d",&y[i][j]);
		}
	}
	cnt=0;
	pos=0;
	for(i=0;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
			if(x[a-1][i]==y[b-1][j])
			{
				cnt++;
				if(cnt>1)
					break;
				pos=x[a-1][i];
				break;
			}
		}
		if(cnt>1)
			break;
	}
	if(cnt==0)
	{
		printf("Case #%d: Volunteer cheated!\n",r);
	}
	else if(cnt==1)
	{
		printf("Case #%d: %d\n",r,pos);
	}
	else
		printf("Case #%d: Bad magician!\n",r);
		r++;
	}
	return 0;
}