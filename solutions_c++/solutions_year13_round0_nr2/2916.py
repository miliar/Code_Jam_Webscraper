#include<cstdio>
#include<cstring>


using namespace std;


int graph[200][200];
int row,col;

bool check(int r,int c)
{
	int i,j;
	bool r_max=true,c_max=true;
	for(i=0;i<row;i++)
	{
		if(graph[i][c]>graph[r][c]) c_max=false;
	}
	for(j=0;j<col;j++)
	{
		if(graph[r][j]>graph[r][c]) r_max=false;
	}
	if(r_max==false && c_max==false) return false;
	else return true;
}

int main(void)
{
	int cas,cases;
	int i,j,k;
	int r,c,n_r,n_c;
	bool flag;
	bool alone;
	
	scanf("%d",&cases);
	for(cas=1;cas<=cases;cas++)
	{
		scanf("%d%d",&row,&col);
		for(i=0;i<row;i++)
			for(j=0;j<col;j++)
				scanf("%d",&graph[i][j]);
		if(row==1 || col==1) 
		{
			printf("Case #%d: YES\n",cas);
			continue;
		}

		for(r=0;r<row;r++)
		{
			for(c=0;c<col;c++)
			{
			   flag=check(r,c);
			   if(!flag) break;  
			}
			if(!flag) break;
		}
		if(flag)printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);
	}
	return 0;
}
