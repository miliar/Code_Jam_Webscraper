#include<iostream>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int t;
int r,c;
char map[200][200];

int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

bool check(int i, int j)
{
	int k;
	for(k=0; k<=3;k++)
	{
		int nowi=i+dx[k], nowj=j+dy[k];
		while(nowi>=0 && nowi <r && nowj >=0 && nowj <c)
		{
			if(map[nowi][nowj] != '.')
				return true;
			nowi+=dx[k];
			nowj+=dy[k];
		}
	}
	return false;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	for(int files=1; files<=t; files++)
	{
		memset(map,0,sizeof(map));
		
		cin>>r>>c;
		int i,j;
		for(i=0;i<r;i++)
		{
			cin>>map[i];
		}
		
		bool ok=true;
		int ans=0;
		for(i=0; i<r;i++)
		{
			for(j=0; j<c; j++)
			{
				if(map[i][j] != '.')
				{
					if(!check(i,j))
					{
						printf("Case #%d: IMPOSSIBLE\n", files);
						ok = false;
						break;
					}
					else
					{
						bool all_point=true;
						if(map[i][j]=='>')
						{
							for(int k=j+1; k<c;k++)
							{
								if(map[i][k] != '.')
								{
									all_point=false;
									break;
								}
							}
						}
						else if(map[i][j] == 'v')
						{
							for(int k=i+1; k<r; k++)
							{
								if(map[k][j] != '.')
								{
									all_point = false;
									break;
								}
							}
						}
						else if(map[i][j] == '<')
						{
							for(int k=j-1; k>=0; k--)
							{
								if(map[i][k] != '.')
								{
									all_point = false;
									break;
								}
							}
						}
						else if(map[i][j] == '^')
						{
							for(int k=i-1; k>=0; k--)
							{
								if(map[k][j] != '.')
								{
									all_point = false;
									break;
								}
							}
						}
						
						if(all_point)
							ans++;
					}
				}
			}
			if(!ok)
				break;
		}
		if(ok)
		{
			printf("Case #%d: %d\n", files, ans);
		}
	}
	//system("pause");
	return 0;
}

