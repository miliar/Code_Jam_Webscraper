#include<stdio.h>
#include<algorithm>

using namespace std;

char mine[55][55];
char cmine[55][55];

void Fill(int rr, int cc, int r, int c)
{
	cmine[rr][cc] = '*';
	if(rr>0 && cmine[rr-1][cc]=='.')
		Fill(rr-1, cc, r, c);
	if(rr>0 && cc>0 && cmine[rr-1][cc-1]=='.')
		Fill(rr-1, cc-1, r, c);
	if(rr>0 && cc<c-1 && cmine[rr-1][cc+1]=='.')
		Fill(rr-1, cc+1, r, c);
	if(cc>0 && cmine[rr][cc-1]=='.')
		Fill(rr, cc-1, r, c);
	if(cc<c-1 && cmine[rr][cc+1]=='.')
		Fill(rr, cc+1, r, c);
	if(rr<r-1 && cmine[rr+1][cc]=='.')
		Fill(rr+1, cc, r, c);
	if(rr<r-1 && cc>0 && cmine[rr+1][cc-1]=='.')
		Fill(rr+1, cc-1, r, c);
	if(rr<r-1 && cc<c-1 && cmine[rr+1][cc+1]=='.')
		Fill(rr+1, cc+1, r, c);
}

int res_r, res_c;

bool NearBomb(int rr, int cc, int r, int c)
{
	if(rr>0 && mine[rr-1][cc]=='*')
		return true;
	if(rr>0 && cc>0 && mine[rr-1][cc-1]=='*')
		return true;
	if(rr>0 && cc<c-1 && mine[rr-1][cc+1]=='*')
		return true;
	if(cc>0 && mine[rr][cc-1]=='*')
		return true;
	if(cc<c-1 && mine[rr][cc+1]=='*')
		return true;
	if(rr<r-1 && mine[rr+1][cc]=='*')
		return true;
	if(rr<r-1 && cc>0 && mine[rr+1][cc-1]=='*')
		return true;
	if(rr<r-1 && cc<c-1 && mine[rr+1][cc+1]=='*')
		return true;
	return false;
}

bool NearEmpty(int rr, int cc, int r, int c)
{
	if(rr>0 && mine[rr-1][cc]=='.')
		return true;
	if(rr>0 && cc>0 && mine[rr-1][cc-1]=='.')
		return true;
	if(rr>0 && cc<c-1 && mine[rr-1][cc+1]=='.')
		return true;
	if(cc>0 && mine[rr][cc-1]=='.')
		return true;
	if(cc<c-1 && mine[rr][cc+1]=='.')
		return true;
	if(rr<r-1 && mine[rr+1][cc]=='.')
		return true;
	if(rr<r-1 && cc>0 && mine[rr+1][cc-1]=='.')
		return true;
	if(rr<r-1 && cc<c-1 && mine[rr+1][cc+1]=='.')
		return true;
	return false;
}

bool checkmine(int r, int c)
{
	bool work = true;
	for(int i=0;i<r && work;i++)
	{
		for(int j=0;j<c && work;j++)
		{
			if(cmine[i][j]=='.')
			{
				Fill(i,j,r,c);
				work = false;
			}
		}
	}
	bool connected = true;
	for(int i=0;i<r && connected;i++)
	{
		for(int j=0;j<c && connected;j++)
		{
			if(cmine[i][j]=='.')
				connected=false;
		}
	}
	if(connected)
	{
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(mine[i][j]=='.' && NearBomb(i,j, r, c))
					mine[i][j] = '#';
				cmine[i][j]=mine[i][j];
			}
		}
		work = true;
		for(int i=0;i<r && work;i++)
		{
			for(int j=0;j<c && work;j++)
			{
				if(cmine[i][j]=='.')
				{
					Fill(i,j,r,c);
					work = false;
				}
			}
		}
		connected = true;
		for(int i=0;i<r && connected;i++)
		{
			for(int j=0;j<c && connected;j++)
			{
				if(cmine[i][j]=='.')
					connected=false;
			}
		}
		if(connected)
		{
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
					cmine[i][j]=mine[i][j];
			}
			work = true;
			for(int i=0;i<r && work;i++)
			{
				for(int j=0;j<c && work;j++)
				{
					if(cmine[i][j]=='#' && !NearEmpty(i,j, r, c))
						return false;
				}
			}
			return true;
		}
	}
	return false;
}

bool fillMine(int r, int c, int m)
{
	int digit = r*c;
	char digits[32];
	digits[digit] = NULL;
	for(int i=0;i<digit;i++)
		digits[i]='.';
	for(int i=0;i<m;i++)
		digits[i]='*';

	do
	{
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				cmine[i][j]=mine[i][j] = digits[i*c+j];
			cmine[i][c]=mine[i][c] = NULL;
		}
		if(m==0 || r*c-m==1) return true;
		if(checkmine(r,c)) return true;
	}while(next_permutation(digits, digits+digit));
	return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int T,R,C,M;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		scanf("%d %d %d",&R,&C,&M);
		bool can = fillMine(R,C,M);
		printf("Case #%d:\n",cs);
		if(can)
		{
			bool found = false;
			for(int i=0;i<R && !found;i++)
			{
				for(int j=0;j<C && !found;j++)
				{
					if(mine[i][j]=='.')
					{
						mine[i][j]='c';
						found = true;
					}
				}
			}

			for(int i=0;i<R;i++)
			{
				for(int j=0;j<C;j++)
				{
					if(mine[i][j]=='#')
						mine[i][j]='.';
				}
			}

			for(int i=0;i<R;i++)
				printf("%s\n",mine[i]);
		}
		else
			printf("Impossible\n");
	}

}