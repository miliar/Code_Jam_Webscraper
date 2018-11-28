// CF 179.cpp: определяет точку входа для консольного приложения.
//

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>

#include<iostream>
#include<sstream>
#include <fstream>

using namespace std;

#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)
#define REPL(i,x) for(int i=0;x[i];i++)
#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define F first
#define S second

#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif

typedef pair<int,int> PII;
typedef long long i64;
typedef unsigned long long u64;

void crocA ()
{
	int n, count = 0;
	map<int, int> sessions;

	cin>>n;
	for (int i = 0; i < n; i++)
	{
		int t;
		cin>>t;
		if (t > 0)
		{
			if (sessions[t] >= 2)
			{
				count = -1;
				break;
			}
			else if (sessions[t] == 1)
			{
				count++;
				sessions[t]++;
			}
			else
			{
				sessions[t] = 1;
			}
		}
	}
	cout<<count;
}

bool checkWin(vector<string>& board, char c)
{
	// Check for X
	bool bX = true;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] != c && board[i][j] != 'T')
			{
				bX = false;
				continue;
			}
		}

		if (bX)
		{
			return bX;
		}		
		bX = true;
	}

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (board[j][i] != c && board[j][i] != 'T')
			{
				bX = false;
				continue;
			}
		}

		if (bX)
		{
			return bX;
		}
		bX = true;
	}

	for (int i = 0; i < 4; i++)
	{
		if (board[i][i] != c && board[i][i] != 'T')
		{
			bX = false;
			break;
		}
	}

	if (bX)
	{
		return bX;
	}
	bX = true;

	for (int i = 0; i < 4; i++)
	{
		if (board[i][3 - i] != c && board[i][3 - i] != 'T')
		{
			bX = false;
			break;
		}
	}

	return bX;
}

string winner(vector<string>& board)
{
	bool res = checkWin(board, 'X');
	if (res)
	{
		return "X won";
	}

	res = checkWin(board, 'O');
	if (res)
	{
		return "O won";
	}

	bool isEnded = true;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] == '.')
			{
				return "Game has not completed";
			}
		}
	}

	return "Draw";
}

int main(int argc, char* argv[])
{
	ifstream fcin("A-large.in");
	ofstream fcout("A-large.out");

	int n;
	vector<string> board(4);

	fcin>>n;
	for (int k = 1; k <= n; k++)
	{
		for (int i = 0; i < 4; i++)
		{
			string t;
			fcin>>t;
			board[i] = t;
		}

		string res = winner(board);
		fcout<<"Case #"<<k<<": "<<res<<endl;
		cout<<"Case #"<<k<<": "<<res<<endl;
	}

	return 0;
}

