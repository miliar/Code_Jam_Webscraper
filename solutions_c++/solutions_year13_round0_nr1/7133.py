#pragma comment(linker, "/STACK:16777216")
#pragma warning (disable : 4786)
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
 
#define maxsize 100010  
   
using namespace std;
 
const double EPS = 1e-11;
const int INF = ( 1<<29 );
const double PI = 2 * acos( 0.0 );
 
int MAX( int a , int b ) { return a > b ? a : b;  }
int MIN( int a , int b ) { return a < b ? a : b;  }
void SWAP( int &a , int &b ) { int t = a; a = b; b = t; }
int GCD( int a , int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

bool cmp(const int &a, const int &b)
{
    if(a<b) return true;
    else return false;
}


void result(int k);
 
 
int main()
{
	freopen ( "input.in", "r", stdin );
	freopen ( "output.out", "w", stdout );
	int test, k;
	scanf("%d", &test);
	for(k=1; k<=test; k++)
		result(k);
	//system("pause");
	return 0;
}
 
void result(int k)
{
	bool dt=false;
	char grid[5][5], turn, tmp[5];
	int i, j, x, o, t, tot, cond=0;

	for(i=0; i<4; i++)
	{
		o=x=t=0;
		scanf("%s", grid[i]);
		for(j=0; j<4; j++)
		{
			if(grid[i][j]=='.')
			{
				dt=true;
				//printf("DOT\n");
			}
			else if(grid[i][j]=='T')
				t++;
			else if(grid[i][j]=='X')
				x++;
			else
				o++;
		}
		//printf("first x= %d, o= %d, t= %d\n", x, o, t);
		if(x==4 || (x==3 && t==1))
		{
			cond=1;
			//printf("11\n");
		}
		if(o==4 || (o==3 && t==1))
		{
			cond=2;
			//printf("12\n");
		}
	}
	gets(tmp);
	if(cond==1)
	{
		printf("Case #%d: X won\n", k);
		return;
	}

	if(cond==2)
	{
		printf("Case #%d: O won\n", k);
		return;
	}


	for(j=0; j<4; j++)
	{
		o=x=t=0;
		for(i=0; i<4; i++)
		{
			if(grid[i][j]=='T')
				t++;
			else if(grid[i][j]=='X')
				x++;
			else if(grid[i][j]=='O')
				o++;
		}
		//printf("second x= %d, o= %d, t= %d\n", x, o, t);
		if(x==4 || (x==3 && t==1))
			cond=1;
		if(o==4 || (o==3 && t==1))
			cond=2;
	}

	if(cond==1)
	{
		printf("Case #%d: X won\n", k);
		return;
	}

	if(cond==2)
	{
		printf("Case #%d: O won\n", k);
		return;
	}

	o=x=t=0;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			if(i==j)
			{
				if(grid[i][j]=='T')
					t++;
				else if(grid[i][j]=='X')
					x++;
				else if(grid[i][j]=='O')
					o++;
			}
		}
	}
	//printf("third x= %d, o= %d, t= %d\n", x, o, t);
	if(x==4 || (x==3 && t==1))
			cond=1;
	if(o==4 || (o==3 && t==1))
		cond=2;

	if(cond==1)
	{
		printf("Case #%d: X won\n", k);
		return;
	}

	if(cond==2)
	{
		printf("Case #%d: O won\n", k);
		return;
	}


	o=x=t=0;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			if(i+j==3)
			{
				if(grid[i][j]=='T')
					t++;
				else if(grid[i][j]=='X')
					x++;
				else if(grid[i][j]=='O')
					o++;
			}
		}
	}
	//printf("fourth x= %d, o= %d, t= %d\n", x, o, t);
	if(x==4 || (x==3 && t==1))
			cond=1;
	if(o==4 || (o==3 && t==1))
		cond=2;

	if(cond==1)
	{
		printf("Case #%d: X won\n", k);
		return;
	}

	if(cond==2)
	{
		printf("Case #%d: O won\n", k);
		return;
	}


	if(dt==false)
		printf("Case #%d: Draw\n", k);
	else
		printf("Case #%d: Game has not completed\n", k);
}