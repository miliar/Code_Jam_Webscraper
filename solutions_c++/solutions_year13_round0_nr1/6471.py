#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <complex>
#include <bitset>
#include <iostream>
using namespace std;
 
//#define NULL 0//
#define PB push_back	//
#define PF push_front
#define CINT (int)		//cast int	
#define CDBL (double)	//cast double
 
//for loops, initialize to zero if unspecified, max/final exclusive
#define FOR(i,max) for(int i=0;i<(int)(max);i++)
#define FORI(i,init,max) for(int i=init;i<(int)(max);i++)
#define FORD(i,init) for(int i=init;i>=0;i--)
#define FORDI(i,init,final) for(int i=init;i>final;i--)
#define FORFOR(rMax,cMax) FOR(j,rMax)FOR(i,cMax)//implicit i's and j's lol
 
//linear algebra
#define ZEROS(T,var,rows,columns) T var[rows][columns]; FORFOR(rows,columns){var[j][i]=0;}
#define DISMAT(var,rows,columns)  FORFOR(rows,columns){cout << var[j][i]<< " "; if(i==columns-1)cout<<endl;}
#define SUM(begin,end) accumulate(begin,end,0)
 
 
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
//#define ZERO(x) memset(x,0,sizeof(x))
#define PI 3.1415926535897932384
 
 
typedef vector<int> VI;
typedef vector<double> VD;
typedef deque<int> DQI;
typedef deque<double> DQD;
 
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MOD 1000000007

int reverse(int n)
{
	int rn=0;
	while(n)
	{
	rn=rn*10+n%10;
	n/=10;
	}
	return rn;
}



int main()
{
	int T;
	char cX='X';
	char cO='O';
	char cT='T';
	char cdot='.';
	
	char X[4][4];
	char O[4][4];
	int casenum=0;
	
	freopen("input.txt","r+",stdin);
	freopen("output.txt","w+",stdout);
	
	scanf("%d\n", &T);
	while(T--)
	{	
		int ndot=0;
		int chx=1;
		int cho=1;
		bool xwon=false;
		bool owon=false;

		for(int j=0; j<4; j++)
		{
			chx=1;
			cho=1;
			for(int i=0; i<4; i++)
			{	
				cin >> X[j][i];
				O[j][i]=X[j][i];
				if(X[j][i]==cdot)
					ndot++;
				else if(X[j][i]==cT)
				{
					X[j][i]=cX;
					O[j][i]=cO;
				}
				if(i>0 &&(X[j][i]==X[j][i-1]) && X[j][i]==cX)
					chx++;
				if(i>0 &&(O[j][i]==O[j][i-1]) && O[j][i]==cO)
					cho++;

			}

			if(chx==4)
				xwon=true;

			if(cho==4)
				owon=true;
			
		}
		for(int i=0; i<4; i++)
		{
			if(X[0][i]==X[1][i]&&X[0][i]==X[2][i]&&X[0][i]==X[3][i]&&X[0][i]==cX)
				xwon=true;
			if(O[0][i]==O[1][i]&&O[0][i]==O[2][i]&&O[0][i]==O[3][i]&&O[0][i]==cO)
				owon=true;
		}

		if(X[0][0]==X[1][1]&&X[0][0]==X[2][2]&&X[0][0]==X[3][3]&&X[0][0]==cX)
			xwon=true;
		if(O[0][0]==O[1][1]&&O[0][0]==O[2][2]&&O[0][0]==O[3][3]&&O[0][0]==cO)
			owon=true;

		if(X[0][3]==X[1][2]&&X[0][3]==X[2][1]&&X[0][3]==X[3][0]&&X[0][3]==cX)
			xwon=true;
		if(O[0][3]==O[1][2]&&O[0][3]==O[2][1]&&O[0][3]==O[3][0]&&O[0][3]==cO)
			owon=true;

		if(xwon)
			printf("Case #%d: %s\n", ++casenum, "X won");
		else if(owon)
			printf("Case #%d: %s\n", ++casenum, "O won");
				
		else if(ndot==0)
			printf("Case #%d: %s\n", ++casenum, "Draw");
		else if(ndot>0)
			printf("Case #%d: %s\n", ++casenum, "Game has not completed");
		
		}

	return 0;
}   