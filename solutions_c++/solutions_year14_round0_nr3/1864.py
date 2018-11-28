#include<cstdio>
#include<cstring>

const int maxn=10;
char map[maxn][maxn];
int R,C,n,S;

bool vis[maxn][maxn];
int dx[8]={-1,-1,-1,0,0,1,1,1};
int dy[8]={-1,0,1,-1,1,-1,0,1};
struct node
{
	int a,b;
}Que[maxn*maxn];
int count=0;

bool bfs(int i,int j)
{
	vis[i][j]=1;
	count--;	
	int front=0,rear=0;
	Que[rear].a=i,Que[rear++].b=j;
	while(front!=rear)
	{
		if(!count)
			return 1;
		int ui=Que[front].a,uj=Que[front++].b;
		bool flag=1;
		for(int k=0;k<8;k++)
		{
			int vi=ui+dx[k],vj=uj+dy[k];
			if( vi<=R&&vi>=1&&vj<=C&&vj>=1&&!vis[vi][vj])
			{
				//printf("%d %d\n",vi,vj);
				if(map[vi][vj]=='*')
				{
					flag=0;
					break;
				}
			}    
		}	
		if(!flag)
			continue;
		//printf("fsd\n");	
		for(int k=0;k<8;k++)
		{
			int vi=ui+dx[k],vj=uj+dy[k];
			if( vi<=R&&vi>=1&&vj<=C&&vj>=1
			    &&!vis[vi][vj]&&map[vi][vj]!='*')
			{
				//printf("%dkk\n",k);
				vis[vi][vj]=1;
				count--;
				Que[rear].a=vi;
				Que[rear++].b=vj;
			}    
		}			
	}
	return 0;
}

int main()
{
	//freopen("3.in","r",stdin);
	//freopen("3.out","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d:\n",t);
		scanf("%d%d%d",&R,&C,&n);
		int M=(1<<(R*C));
		for(int x=0;x<M;x++)
		{
			int tep=x,cnt=0;
			while(tep)
			{
				if(tep&1)cnt++;
				tep>>=1;
			}
			if(cnt!=n)continue;
			//printf("%d\n",tep);
			tep=x;
			for(int i=1;i<=R;i++)
			{
				for(int j=1;j<=C;j++)
				{
					if(tep&1)map[i][j]='*';
					else     map[i][j]='.';
					tep>>=1;
					//printf("%c",map[i][j]);
				}
				map[i][C+1]=0;
			}	
			//printf("\n");
			for(int i=1;i<=R;i++)
				for(int j=1;j<=C;j++)
					if(map[i][j]=='.')
					{
						memset(vis,0,sizeof(vis));
						count=R*C-n;
						//printf("%d %d %d\n",count,i,j);
						if(bfs(i,j))
						{
							map[i][j]='c';
							for(int k=1;k<=R;k++)
								printf("%s\n",&map[k][1]);
							goto A;	
						}
					}
		}
		printf("Impossible\n");
		A:;
	}
	return 0;
}