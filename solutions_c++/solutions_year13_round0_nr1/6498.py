#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <limits>

using namespace std;

#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define REP(I,N) FOR(I,0,N)
#define S(N) scanf("%d", &N)
#define SL(N) scanf("%lld", &N)
#define PB push_back
#define MP make_pair
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define cell pair<int,int>
#define edge pair<int, cell>
typedef vector<string> vs;
typedef long long int LL;
typedef vector<int> vi;
typedef vector<LL> vii;
int main()
{
	int t;S(t);
	REP(c,t)
	{
		int d;
		printf("Case #%d: ",c+1);
		char a[4][4];
		REP(i,4)
			REP(j,4)
				cin>>a[i][j];
		REP(i,4)
		{
			d=0;
			REP(j,4)
			{
				if(a[i][j]=='X'||a[i][j]=='T')
					d++;
			}
			if(d==4)
			{
				printf("X won\n");
				break;
			}
		}
		if(d==4)continue;
		REP(i,4)
		{
			d=0;
			REP(j,4)
			{
				if(a[j][i]=='X'||a[j][i]=='T')
					d++;
			}
			if(d==4)
			{
				printf("X won\n");
				break;
			}
		}
		if(d==4)continue;
		d=0;
		REP(i,4)
		{
			if(a[i][i]=='X'||a[i][i]=='T')
					d++;
			if(d==4)
			{
				printf("X won\n");
				break;
			}
		}
		if(d==4)continue;
		d=0;
		REP(i,4)
		{
			if(a[i][3-i]=='X'||a[i][3-i]=='T')
					d++;
			if(d==4)
			{
				printf("X won\n");
				break;
			}
		}
		if(d==4)continue;
		REP(i,4)
		{
			d=0;
			REP(j,4)
			{
				if(a[i][j]=='O'||a[i][j]=='T')
					d++;
			}
			if(d==4)
			{
				printf("O won\n");
				break;
			}
		}
		if(d==4)continue;
		REP(i,4)
		{
			d=0;
			REP(j,4)
			{
				if(a[j][i]=='O'||a[j][i]=='T')
					d++;
			}
			if(d==4)
			{
				printf("O won\n");
				break;
			}
		}
		if(d==4)continue;
		d=0;
		REP(i,4)
		{
			if(a[i][i]=='O'||a[i][i]=='T')
					d++;
			if(d==4)
			{
				printf("O won\n");
				break;
			}
		}
		if(d==4)continue;
		d=0;
		REP(i,4)
		{
			if(a[i][3-i]=='O'||a[i][3-i]=='T')
					d++;
			if(d==4)
			{
				printf("O won\n");
				break;
			}
		}	
		if(d==4)continue;
		d=0;
		REP(i,4)	
			REP(j,4)
				if(a[i][j]=='.'){d=1;break;}
		if(d==1)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}  
