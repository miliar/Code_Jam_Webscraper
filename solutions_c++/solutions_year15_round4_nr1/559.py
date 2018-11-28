#include <cstdio>

char array[200][200];

int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

int dat[256];

bool inbound(int a, int b, int r, int c)
{
	return a>=0 && a<r && b>=0 && b<c;
}

int main()
{
	dat['.'] = -1;
	dat['^'] = 2;
	dat['>'] = 1;
	dat['<'] = 3;
	dat['v'] = 0;
	int t;
	scanf("%d",&t);

	for(int casenum=1; casenum<=t; casenum++)
	{
		int r,c;
		scanf("%d %d",&r,&c);
		for(int i=0; i<r; i++)
		{
			scanf("%s",array[i]);
			for(int j=0; j<c; j++)
			{
				array[i][j] = dat[array[i][j]];
			}
		}

		bool valid = true;
		int total = 0;
		for(int i=0; i<r && valid; i++)
			for(int j=0; j<c && valid; j++)
			{
				if(array[i][j]>=0)
				{
					int dir = array[i][j];
					int xpos = i+dx[dir];
					int ypos = j+dy[dir];
					while(inbound(xpos,ypos,r,c))
					{
						if(array[xpos][ypos]>=0)
							break;
						xpos += dx[dir];
						ypos += dy[dir];
					}

					//printf("%d %d %d %d\n",i,j,xpos,ypos);

					if(!inbound(xpos,ypos,r,c))
					{
						valid = false;
						for(dir = 0; dir<4; dir++)
						{
							if(dir==array[i][j])
								continue;
							xpos = i+dx[dir];
							ypos = j+dy[dir];
							while(inbound(xpos,ypos,r,c))
							{
								if(array[xpos][ypos]>=0)
									break;
								xpos += dx[dir];
								ypos += dy[dir];
							}

							if(inbound(xpos,ypos,r,c))
							{
								valid = true;
								total++;
								break;
							}
						}
					}
				}
			}
		if(!valid)
			printf("Case #%d: IMPOSSIBLE\n",casenum);
		else
			printf("Case #%d: %d\n",casenum,total);
	}
}