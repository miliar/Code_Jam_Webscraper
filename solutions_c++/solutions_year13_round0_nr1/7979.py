#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include<fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#define rep(x,n) for(int x=0;x<n;++x)
#define rep1(i,s) for(int i = 0; i < (int)s.size(); ++i)
#define mem(a, b) memset(a, b, sizeof(a))

#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define xetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
#define oo (int)10e7
#define rd(x) scanf("%d", &x)
#define rdfile(x) freopen(x, "r", stdin)
#define wtfile(x) freopen(x, "w", stdout)
using namespace std;

#define negmod(x, mod) ((x + mod) % mod)

char grid[4][4];
char whoWins()
{
	//Rows Matching
	for(int i=0;i<4;++i)
	{
		char resultofThree_1=grid[i][0] & grid[i][1] & grid[i][2];
		char resultofThree_2=grid[i][1] & grid[i][2] & grid[i][3];
		if(resultofThree_1 == 'X' || resultofThree_1 == 'O')
		{
			if(grid[i][3] == 'T' || grid[i][3] == resultofThree_1)
				return resultofThree_1;
		}
		else
			if(resultofThree_2 == 'X' || resultofThree_2 == 'O')
			{
				if(grid[i][0] == 'T' || grid[i][0] == resultofThree_2)
					return resultofThree_2;
			}
	}
	//Coloumns Matching
	for(int i=0;i<4;++i)
	{
		char resultofThree_1=grid[0][i] & grid[1][i] & grid[2][i];
		char resultofThree_2=grid[1][i] & grid[2][i] & grid[3][i];
		if(resultofThree_1 == 'X' || resultofThree_1 == 'O')
		{
			if(grid[3][i] == 'T' || grid[3][i] == resultofThree_1)
				return resultofThree_1;
		}
		else
			if(resultofThree_2 == 'X' || resultofThree_2 == 'O')
			{
				if(grid[0][i] == 'T' || grid[0][i] == resultofThree_2)
					return resultofThree_2;
			}	
	}
	//Diagonal 1 Matching
	char first_diagonal_resultofThree_1=grid[0][0] & grid[1][1] & grid[2][2];
	char first_diagonal_resultofThree_2=grid[1][1] & grid[2][2] & grid[3][3];
	if(first_diagonal_resultofThree_1 == 'X' || first_diagonal_resultofThree_1 == 'O')
	{
		if(grid[3][3] == 'T' || grid[3][3] == first_diagonal_resultofThree_1)
			return first_diagonal_resultofThree_1;
	}
	else
		if(first_diagonal_resultofThree_2 == 'X' || first_diagonal_resultofThree_2 == 'O')
		{
			if(grid[0][0] == 'T' || grid[0][0] == first_diagonal_resultofThree_2)
				return first_diagonal_resultofThree_2;
		}

		//Diagonal 2 Matching
		char second_diagonal_resultofThree_1=grid[3][0] & grid[2][1] & grid[1][2];
		char second_diagonal_resultofThree_2=grid[2][1] & grid[1][2] & grid[0][3];
		if(second_diagonal_resultofThree_1 == 'X' || second_diagonal_resultofThree_1 == 'O')
		{
			if(grid[0][3] == 'T' || grid[0][3] == second_diagonal_resultofThree_1)
				return second_diagonal_resultofThree_1;
		}
		else
			if(second_diagonal_resultofThree_2 == 'X' || second_diagonal_resultofThree_2 == 'O')
			{
				if(grid[3][0] == 'T' || grid[3][0] == second_diagonal_resultofThree_2)
					return second_diagonal_resultofThree_2;
			}
			return 'T';
}
bool drawOrNot()
{
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			if(grid[i][j] == '.')
				return false;
	return true;
}
int main()
{
	//rdfile("A-small-attempt0.in");
	//wtfile("output.txt");
	string emptystring; 
	int testcases;
	cin>>testcases;
	for(int T=1;T<=testcases;++T)
	{
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>grid[i][j];
		char winner = whoWins();
		if(winner != 'T')
			printf("Case #%d: %c won\n",T,winner);
		else
		{
			printf("Case #%d: %s\n",T,(drawOrNot() ? "Draw" : "Game has not completed")); 
		}
		cin.ignore();
		getline(cin,emptystring);
	}
	return 0;
}