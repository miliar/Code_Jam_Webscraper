#include <set>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <iomanip>
#include <map>
#include <cmath>
#include <algorithm>

#define _DEBUG 0
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))


using namespace std;

/************
general types
*************/

typedef set<int> tSet[4];
typedef unsigned int uint;
typedef enum { OK } tenResultType;

/*****************
input type
****************/

typedef struct
{
	unsigned int A,B,K;
} tstInput;

/***************
result type
*****************/

typedef struct
{
	tenResultType type;
	int no;
} tstResult;

/****************
input getter
******************/

void vGetInput(tstInput & in)
{
	int i,j,k;
	int n;
	cin >> in.A >> in.B >> in.K;
	
}

/*******************
result getter
********************/
		
void vGetResult(tstInput & in, tstResult & out)
{
	int i, j, k;
	int count = 0;
	for (i = 0; i<in.A; ++i)
	{
		for (j=0; j<in.B; ++j)
		{
			if ((i&j) < in.K)
				++count;
		}
	}
	
	out.no = count;
	
	
	
	
	

}

/*******************
result printer
********************/

void vPrintResult(int c, tstResult & r)
{
	cout << "Case #" << c << ": ";
	switch (r.type)
	{
		// case a:
			// cout << r.no;
			// break;
		default:
			cout << r.no;
			break;
	}
	cout << endl;		
}

/*******************
driver
********************/

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i=1;i<=n;++i)
	{
		tstInput in;
		tstResult res;
		vGetInput(in);
		vGetResult(in, res);
		vPrintResult(i, res);
	}

	return 0;
}