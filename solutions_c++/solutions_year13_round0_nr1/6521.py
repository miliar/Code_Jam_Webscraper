#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <streambuf>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>

#define all(x) (x).begin(),(x).end() 
#define sz(v) ((int) v.size())
#define mp make_pair 
#define fori(type,x,a,b) for( type (x) = (a) ; (x) < (b) ; (x)++) 
#define forr(type,x,a,b) for( type (x) = (a) ; (x) >= (b) ; (x)--) 
#define fi(x,a,b) fori(int,x,a,b) 
#define fri(x,a,b) forr(int,x,a,b) 
#define fll(x,a,b) fori(long long,x,a,b) 
#define frll(x,a,b) forr(long long,x,a,b) 
#define fill(x,v,n) memset((x),(v),n*sizeof(x)); 
#define pb(x) push_back(x)

#define p(x) cout << x << " "
#define pl cout << endl
#define pn(x) cout << #x <<": "<< x << endl

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#if 1
string whoWon(int count[3])
{
	if (count[0] == 4 || (count[0] == 3 && count[2] > 0))
		return "X won";
	if (count[1] == 4 || (count[1] == 3 && count[2] > 0))
		return "O won";
	return "";
}
string find(vector<string> board)
{
	bool isBlankPresent = false;
	fi(i,0,board.size())
	{
		int count[3] =
		{	0,0,0};
		fi(j,0,board[i].size())
		if(board[i][j] == 'X') count[0]++;
		else if(board[i][j] == 'O') count[1]++;
		else if(board[i][j] == 'T') count[2]++;
		else isBlankPresent = true;
		if(whoWon(count) != "") return whoWon(count);
	}

	fi(j,0,board[0].size())
	{
		int count[3] =
		{	0,0,0};
		fi(i,0,board.size())
		{
			if(board[i][j] == 'X') count[0]++;
			else if(board[i][j] == 'O') count[1]++;
			else if(board[i][j] == 'T') count[2]++;
			else isBlankPresent = true;

			if(whoWon(count) != "") return whoWon(count);
		}
	}
	int count[3] =
	{ 0, 0, 0 };
	fi(i,0,board.size())
	{
		if(board[i][i] == 'X') count[0]++;
		else if(board[i][i] == 'O') count[1]++;
		else if(board[i][i] == 'T') count[2]++;
		else isBlankPresent = true;
	}
	if (whoWon(count) != "")
		return whoWon(count);

	int j=board[0].size()-1;
	count[0] = count[1] = count[2] = 0;
	fi(i,0,board.size())
	{
		if(board[i][j] == 'X') count[0]++;
		else if(board[i][j] == 'O') count[1]++;
		else if(board[i][j] == 'T') count[2]++;
		else isBlankPresent = true;
		j -= 1;
	}
	if (whoWon(count) != "")
		return whoWon(count);

	if (!isBlankPresent)
		return "Draw";
	return "Game has not completed";
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
#endif
	int n;
	cin>>n;

	fi(t,0,n)
	{

		vector<string> board(4);
		fi(i,0,4) cin>>board[i];
		cout<<"Case #"<<t+1<<": "<<find(board)<<endl;
	}
	return 0;
}
#endif
