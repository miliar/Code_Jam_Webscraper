#include<cstdio>
#include<vector>

const int HMAX=10;
const int WMAX=10;

int H,W,M;
bool IsMine[HMAX][WMAX];
int Danger[HMAX][WMAX];
bool Visit[HMAX][WMAX];

inline int PAIR(int i,int j) {return i<<10|j;}
inline int FRST(int k) {return k>>10;}
inline int SCND(int k) {return k&1023;}

bool check()
{
static int C;
	static std::vector<int> Stack;
	int si=-1,sj=-1;
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			if(IsMine[i][j]){Danger[i][j]=-1;continue;}
			Danger[i][j]=0;
			if(i-1>=0)
			{
				if(j-1>=0)Danger[i][j]+=IsMine[i-1][j-1];
				;;;;;;;;;;Danger[i][j]+=IsMine[i-1][j  ];
				if(j+1< W)Danger[i][j]+=IsMine[i-1][j+1];
			}
			if(j-1>=0)Danger[i][j]+=IsMine[i  ][j-1];
			if(j+1< W)Danger[i][j]+=IsMine[i  ][j+1];
			if(i+1< H)
			{
				if(j-1>=0)Danger[i][j]+=IsMine[i+1][j-1];
				;;;;;;;;;;Danger[i][j]+=IsMine[i+1][j  ];
				if(j+1< W)Danger[i][j]+=IsMine[i+1][j+1];
			}
			if(Danger[i][j]==0){si=i;sj=j;}
		}
	}
	if(si<0)return false;
	int _si=si,_sj=sj;
	int k=0;
	for(int i=0;i<H;i++)for(int j=0;j<W;j++)Visit[i][j]=false;
	Visit[si][sj]=true;
	Stack.push_back(PAIR(si,sj));
	do
	{
		k++;
		si=FRST(Stack.back());
		sj=SCND(Stack.back());
		Stack.pop_back();
		if(Danger[si][sj]!=0)continue;
		for(int i=-1;i<=+1;i++)
		{
			if(si+i<0||si+i>=H)continue;
			for(int j=-1;j<=+1;j++)
			{
				if(sj+j< 0)continue;
				if(sj+j>=W)break;
				if(Visit[si+i][sj+j])continue;
				Visit[si+i][sj+j]=true;
				Stack.push_back(PAIR(si+i,sj+j));
			}
		}
	} while(!Stack.empty());
	if(k+M!=H*W)return false;
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			if(i==_si&&j==_sj)putchar('c');
			else putchar(IsMine[i][j]?'*':'.');
		}
		putchar('\n');
	}
	return true;
}

bool dfs(int i,int j,int mine,int space)
{
	if(j==W){j=0;if(++i==H)return check();}
	if(mine !=0){IsMine[i][j]=true ;if(dfs(i,j+1,mine-1,space))return true;}
	if(space!=0){IsMine[i][j]=false;if(dfs(i,j+1,mine,space-1))return true;}
	return false;
}

bool solve()
{
	if(M==0)
	{
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)putchar(i!=0||j!=0?'.':'c');
			putchar('\n');
		}
		return true;
	}
	if(M==H*W-1)
	{
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)putchar(i!=0||j!=0?'*':'c');
			putchar('\n');
		}
		return true;
	}
	return dfs(0,0,M,H*W-M);
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d%d",&H,&W,&M);
		printf("Case #%d:\n",t);
		if(!solve())puts("Impossible");
	}
	return 0;
}
