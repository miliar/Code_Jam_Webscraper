#include <bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define MP make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

int dx[4]={ 0, 1, 0,-1};
int dy[4]={ 1, 0,-1, 0};
char s[150][150];

int main()
{
	int NumberOfTestcases;
	scanf("%d",&NumberOfTestcases);
	int R,C;
	for(int CaseNumber=1;CaseNumber<=NumberOfTestcases;CaseNumber++)
	{
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
			scanf("%s",s[i]);
		/*for(int i=0;i<R;i++)
			for(int j=0;j<R;j++)
				printf("s[%d][%d]:%c\n",i,j,s[i][j]);*/
		int ans=0,d;
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				if(s[i][j]!='.')
				{
					int x,y,ax,ay;
					x=i,y=j;
					bool safe=0;
					switch(s[i][j])
					{
						case '>': ax=0,ay=1; break;
						case 'v': ax=1,ay=0; break;
						case '<': ax=0,ay=-1; break;
						case '^': ax=-1,ay=0; break;
						default: printf("\n(%d %d)\n",i,j),assert(0);
					}
					x+=ax,y+=ay;
				//	printf("[%d %d]\n",i,j);
					while(x>=0 && x<R && y>=0 && y<C)
					{
						//printf("%d %d\n",x,y);
						if(s[x][y]!='.')
							safe=1;
						x+=ax,y+=ay;
					}
					if(!safe)
					{
						for(int k=0;k<4;k++)
						{
							x=i,y=j;
							x+=dx[k],y+=dy[k];
							bool good=0;
							while(x>=0 && x<R && y>=0 && y<C)
							{
								if(s[x][y]!='.')
									good=1;
								x+=dx[k],y+=dy[k];
							}
							if(good)
							{
								ans++;
								safe=1;
								break;
							}
						}
					}
					if(!safe)
						ans=-1;
				}
			}
		printf("Case #%d: ",CaseNumber);
		if(ans==-1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
	return 0;
}
