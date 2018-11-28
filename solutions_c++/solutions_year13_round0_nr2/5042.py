#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;


int Minimum(int a,int b,int c)
{
	return min(min(a,b),min(b,c));
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int ix=1;ix<=t;ix++)
	{
		int m,n;
		scanf("%d %d",&m,&n);
		int lawn[101][101],lawn1[101][101];
		memset(lawn1,100,sizeof(lawn1));
		
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				scanf("%d",&lawn[i][j]);
		int maxrow[101]={0},maxcol[101]={0};
		for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
		{

			if(lawn[i][j]>maxrow[i])
				maxrow[i]=lawn[i][j];
			if(lawn[i][j]>maxcol[j])
				maxcol[j]=lawn[i][j];
			//printf("%d %d %d %d\n",i,j,maxrow[i],maxcol[j]);
		}
		//for(int i=0;i<m;i++)
		//	printf("%d %d\n",maxrow[i],maxcol[i]);
		bool yes=true;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
			{
				lawn1[i][j]=Minimum(lawn1[i][j],maxrow[i],maxcol[j]);
			}
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				if(lawn[i][j]!=lawn1[i][j])
				{
					yes=false;
					break;
				}
		printf("Case #%d: ",ix);
		if(yes)
			printf("YES\n");
		else
			printf("NO\n");
	}
}