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
	int T,A,B;
	int casenum=0;
	freopen("input.txt","r+",stdin);
	freopen("output.txt","w+",stdout);
	
	
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d %d", &A,&B);
		int fsnum=0;
		for(int i=A; i<=B; i++)
		{
			double sqrtnum=sqrt((double)i);
			if(i==reverse(i) && (int)sqrtnum==reverse(sqrtnum) && sqrtnum-(double)(int)sqrtnum==0.0)
				fsnum++;
		}
		printf("Case #%d: %d\n", ++casenum, fsnum);
	}

	return 0;
}   