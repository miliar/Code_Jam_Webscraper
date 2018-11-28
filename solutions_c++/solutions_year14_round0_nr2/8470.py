#include <string>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <cassert>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define FORD(k,a,b) for(int k(b-1); k >= (a); --k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))

typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<string> VS;

int main()
{
#ifdef HOME
	freopen ("B-large.in","r",stdin);
	freopen ("B-large.out","w",stdout);
#endif 
	int T;
	double C,F,X;
	scanf("%d",&T);
	FOR(tc,1,T+1)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		double actF=2;
		double res=X/2;
		double pos=0;
		while(1)
		{
			pos+=C/actF;
			actF+=F;
			double curr = pos + X/actF;
			if(curr<res)
			{
				res = curr;
			}
			else 
				break;
		}
		printf("Case #%d: %.7f\n",tc,res);
	}
	return 0;

}

/*
// color 4-6
// boardsize 8-16
// seed 1- (2^31-2)


struct SquareRemover
{
	const LL seedMultiplier = 48271;
	const LL seedModulo = 2147483647;
	const int stepCounter = 10000;

	VL stepModulo;
	static int boardSize;
	static int colSize;
	//board
	struct BOARD
	{
		int* data;
		LL actseed;
		BOARD(int* _d, int seed)
		{
			data = _d;
			actseed = seed;
		}

		int stepSeed()
		{
			actseed = (actseed * seedMultiplier) % seedModulo;
			return actseed % colSize;
		}

		int step()
		{
			bool found = 0;
			int res=0;
			do{
				found=0;
				REP(row,boardSize-1)
				REP(col,boardSize-1)
				{
					int a=row*boardSize+col;
					if(data[a]==data[a+1] && data[a]==data[a+row] && data[a]==data[a+row+1])
					{ 
						found=1;
						data[a]=stepSeed();
						data[a+1]=stepSeed();
						data[a+2]=stepSeed();
						data[a+3]=stepSeed();
						++res;
						break;
					}
				}
			}while(found);
			return res;
		}
	};



	VI playIt(int col, const VS& board, int seed)
	{
		colSize = col;
		boardSize=board.size();
		stepModulo.reserve(stepCounter);
		stepModulo.push_back(seed);
	}
};

int SquareRemover::colSize;
int SquareRemover::boardSize;

int main()
{


	return 0;
}*/