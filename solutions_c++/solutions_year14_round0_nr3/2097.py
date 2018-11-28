#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
#define pii pair<int,int>

char v[64][64];
bool found;
int R, C, M;
int iii, jjj;

void print_v()
{
	v[iii][jjj] = 'c';
	for(int i = 1; i <= R; i ++)
	{
		for(int j = 1; j <= C; j ++)
			cout << v[i][j];
		cout << endl;
	}
	// cout << endl;
}

void f(int bomb)
{
	// print_v();
	// cout << endl;
	
	if(bomb == M)
	{
		if(found != true)
			print_v();
		found = true;
		return;
	}
	if(found == true || bomb < M)
		return;
		
	
	for(int i = 1; i <= R; i ++)
		for(int j = 1; j <= C; j ++)
		{
			if(v[i][j] == '.')	// can have zero bombs in his neighbor
			{
				vector <pii> here;
				for(int x = i-1; x <= i+1; x ++)
					for(int y = j-1; y <= j+1; y ++)
						if(x >= 1 && x <= R && y >= 1 && y <= C && v[x][y] == '*')
						{
							here.push_back( pii(x, y) );
							v[x][y] = '.';
						}
				if(here.size() != 0)
				{
					bomb -= here.size();
					f(bomb);
					if(found == true)
						return;
					for(int h = 0; h < here.size(); h ++)
					{
						v[here[h].first][here[h].second] = '*';
					}
					bomb += here.size();
				}
			}
		}
}

int main()
{
	int test;
	
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		cin >> R >> C >> M;
		
		printf("Case #%d:\n", cas);
		int mn = min(R, C);
		int empty = R*C - M;
		if(mn == 1)
		{
			if(R == 1)
			{
				for(int j = 1; j <= M; j ++)
					cout << '*';
				for(int j = M+1; j < C; j ++)
					cout << '.';
				cout << 'c' << endl;
			}
			else if(C == 1)
			{
				for(int i = 1; i <= M; i ++)
					cout << '*' << endl;
				for(int i = M+1; i < R; i ++)
					cout << '.' << endl;
				cout << 'c' << endl;
			}			
		}
		else
		{
			found = false;
			for(int i = 1; i <= (R+1)/2; i ++)
				for(int j = 1; j <= (C+1)/2; j ++)
				{
					for(int r = 1; r <= R; r ++)
						for(int c = 1; c <= C; c ++)
							v[r][c] = '*';
					
					iii = i;
					jjj = j;
					v[i][j] = '.';
					f(R*C-1);
					if(found == true)
					{
						v[i][j] = 'c';
						break;
					}
				}
			if(found == false)
				cout << "Impossible" << endl;
		}
	}
	
	return 0;
}