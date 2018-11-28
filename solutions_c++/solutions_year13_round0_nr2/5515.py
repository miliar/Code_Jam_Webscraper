#include <cstdio>
#include <cstring>

int map[101][101];
int qt[101];
int t,n,m,nv;

int main()
{
	scanf(" %d",&t);
	for(int i=1; i<=t; i++)
	{
		int min=101,max=0;
		scanf(" %d %d",&n,&m);
		memset(qt,0,101*sizeof(int));
		for(int j=0; j<n; j++)
			for(int k=0; k<m; k++)
			{
				scanf(" %d",&map[j][k]);
				qt[map[j][k]]++;
				if(map[j][k]<min) min = map[j][k];
				if(map[j][k]>max) max = map[j][k];
			}/*
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
				printf("%d ",map[j][k]);
			printf("\n");
		}				
		printf("DEBUG: %d\n",max);*/
		for(int j=1; j<max; j++) 
		{
			qt[j+1]+=qt[j];
			//printf("DEBUG: %d\n",qt[j]);
		}//printf("DEBUG: %d\n",qt[max]);
		int j;
		for(j=min; j<=max; j++)
		{
			if(qt[j]==0) continue;
			nv = 0;
			for(int k=0; k<n; k++)
				if(map[k][0]<=j)
				{
					int l;
					for(l=0; map[k][l]<=j && l<m; l++);
					if(l==m)
					{
						nv++;
						qt[j]-=m;
					}
					//printf("DEBUG: %d %d %d\n",j,k,nv);
				}		
			//printf("DEBUG: %d %d\n",qt[1],qt[2]);		
			for(int k=0; k<m; k++)
				if(map[0][k]<=j)
				{
					int l;
					for(l=0; map[l][k]<=j && l<n; l++);
					if(l==n)
						qt[j]-=n-nv;
				}		
			//printf("DEBUG: %d %d\n",qt[1],qt[2]);
			if(qt[j]) break;			
		}
		printf("Case #%d: %s\n",i,qt[j]?"NO":"YES");
	}
	return 0;
}
