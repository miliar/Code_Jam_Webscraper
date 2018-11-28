#include <stdio.h>
#include <vector>
#define n 4

using namespace std;

vector<vector<char> > A(4,4);
int T;
bool D;

inline void get_data()
{
	int i, j;
	D=0;
	for(i=0; i<n; i++)
	{
		for(j=0; j<n; j++)
		{
			scanf("%c", &A[i][j]);
			if(A[i][j]=='.')
				D=1;
		}
		scanf("\n");
	}
	scanf("\n");
}

inline int row(int r)
{
	int i;
	char c;

	c=A[r][0];
	if(c=='T')
		c=A[r][1];
	else if(c!='X' && c!='O')
		return 0;
	for(i=1; i<n; i++)
		if(A[r][i]!=c && A[r][i]!='T')
			return 0;
	if(c=='X')
		return 1;
	return 2;
}

inline int col(int col)
{
	int i;
	char c;

	c=A[0][col];
	if(c=='T')
		c=A[1][col];
	else if(c!='X' && c!='O')
		return 0;
	for(i=1; i<n; i++)
		if(A[i][col]!=c && A[i][col]!='T')
			return 0;
	if(c=='X')
		return 1;
	return 2;	
}

inline int diag()
{
	char c;
	int i;

	c=A[0][0];
	if(c=='T')
		c=A[2][2];
	else if(c!='X' && c!='O')
		return 0;
	for(i=1; i<4; i++)
		if(A[i][i]!=c && A[i][i]!='T')
			return 0;
	if(c=='X')
		return 1;
	return 2;
}

inline int diagg()
{
	int i, j;
	char c;

	c=A[0][3];
	if(c=='T')
		c=A[1][2];
	else if(c!='X' && c!='O')
		return 0;
	i=1;
	j=2;
	while(j>=0)
	{
		if(A[i][j]!=c && A[i][j]!='T')
			return 0;
		i++;
		j--;
	}
	if(c=='X')
		return 1;
	return 2;
}

int main()
{
	int i, j;
	int win;
	int d1, d2;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("tac.txt","w",stdout);

	scanf("%d\n", &T);

	for(i=0; i<T; i++)
	{
		get_data();
		printf("Case #%d: ", i+1);
		d1=diag();
		d2=diagg();
		if(d1==1 || d2==1)
			printf("X won\n");

		else if(d1==2 || d2==2)
			printf("O won\n");

		if(d1==0 && d2==0)
			for(j=0; j<n; j++)
			{
				win=row(j);
				if(win==1)
				{
					printf("X won\n");
					break;
				}
				else if(win==2)
				{
					printf("O won\n");
					break;
				}
				win=col(j);
				if(win==1)
				{
					printf("X won\n");
					break;
				}
				else if(win==2)
				{
					printf("O won\n");
					break;
				}
			}
		if(win==0 && D==1)
			printf("Game has not completed\n");
		else if(win==0 && D==0)
			printf("Draw\n");
	}
	return 0;
}


		
