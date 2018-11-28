#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

void Solve()
{
	int R,C,r,c;
	cin >> R >> C;
	char M[R+1][C+1];
	for (r=1; r<=R; r++)
	{
		for (c=1; c<=C; c++)
		{
			cin >> M[r][c];
		}
	}
	int OK,q;
	for (r=1; r<=R; r++)
	{
		for (c=1; c<=C; c++)
		{
			if (M[r][c]!='.')
			{
				OK = 0;
				for (q=1; q<=R; q++)
				{
					if (M[q][c] != '.') OK++;
				}
				for (q=1; q<=C; q++)
				{
					if (M[r][q] != '.') OK++;
				}
				if (OK == 2)
				{
					cout << "IMPOSSIBLE";
					return;
				}
			}
		}
	}
	int answer=0;
	for (r=1; r<=R; r++)
	{
		for (c=1; c<=C; c++)
		{
			if (M[r][c]=='>')
			{
				OK = false;
				for (q=c+1; q<=C; q++)
				{
					if (M[r][q] != '.')
					{
						OK = true;
						break;
					}
				}
				if (!OK) answer++;
			}
			
			if (M[r][c]=='<')
			{
				OK = false;
				for (q=c-1; q>=1; q--)
				{
					if (M[r][q] != '.')
					{
						OK = true;
						break;
					}
				}
				if (!OK) answer++;
			}
			
			if (M[r][c]=='^')
			{
				OK = false;
				for (q=r-1; q>=1; q--)
				{
					if (M[q][c] != '.')
					{
						OK = true;
						break;
					}
				}
				if (!OK) answer++;
			}
			
			if (M[r][c]=='v')
			{
				OK = false;
				for (q=r+1; q<=R; q++)
				{
					if (M[q][c] != '.')
					{
						OK = true;
						break;
					}
				}
				if (!OK) answer++;
			}
		}
	}
	cout << answer;
}
int main()
{
	int q,t;
	cin >> t;
	for (q=0; q<t; q++)
	{
		cout << "Case #" << q+1 << ": "; 
		Solve();
		cout << "\n";
	}
	return 0;
}
