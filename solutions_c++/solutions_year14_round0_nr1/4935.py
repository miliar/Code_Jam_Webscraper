#include <iostream>
using namespace std;
int main()
{
	int n,p,o,j,t,i,s,flag;
	int a[4][4],b[4][4];
	scanf("%d",&t);
	for(o=1;o<=t;o++)
	{	scanf("%d",&n);
		for(i=0;i<4;i++)
		{	for(j=0;j<4;j++)
			scanf("%d",&a[i][j]);
		}
		n--;
		scanf("%d",&p);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&b[i][j]);
		p--;
		flag=0;
		for(i=0;i<4;i++)
		{	for(j=0;j<4;j++)
			if(a[n][i]==b[p][j])
			{	flag++;
				s=a[n][i];
			}
		}
		if(flag==1)
			{	printf("Case #%d: %d\n",o,s);
			}
		if(flag==0)
		{		printf("Case #%d: Volunteer cheated!\n",o);
		}
		if(flag>1)
		{	printf("Case #%d: Bad magician!\n",o);
		}
	}
	return 0;
}