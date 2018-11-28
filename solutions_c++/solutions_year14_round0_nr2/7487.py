#include <set>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <iomanip>
#include <map>

#define _DEBUG 0

using namespace std;

/************
general types
*************/

typedef set<int> tSet[4];
typedef enum { a } tenResultType;

/*****************
input type
****************/

typedef struct
{
	double c;
	double f;
	double x;
} tstInput;

/***************
result type
*****************/

typedef struct
{
	tenResultType type;
	double num;
} tstResult;

/****************
input getter
******************/

void vGetInput(tstInput & in)
{
	cin >> in.c >> in.f >> in.x;	
}

/*******************
result getter
********************/

double fGetEndTime(double cur, double rate, double f, double target)
{
	double c1, c2;

	c1 = c2 = cur;
	
	

}

void vGetResult(tstInput & in, tstResult & out)
{
	//out.num = fGetEndTime(0, in.c, in.f, in.x
	double t=0, t_proj, t_min;
	double rate = 2;
	double cur=0;
	
	t_min = in.x / rate;
	t += in.c / rate;
	cur += rate * t;
	while (t < t_min)
	{
		//if (cur >= in.c)
		//{
			cur -= in.c;
			rate += in.f;
			t_proj = (in.x - cur + rate*t)/rate;
			if (t_proj < t_min)
			{
				t_min = t_proj;
			}
		//}
#if _DEBUG
printf("t=%f: c=%f, %f, %f\n", t, cur, t_proj, t_min);
#endif
		
		t += (in.c - cur )/rate;
		cur += (in.c - cur);
	}
	
	out.num = t_min;	
}

/*******************
result printer
********************/

void vPrintResult(int c, tstResult & r)
{
	cout << "Case #" << c << ": ";
	cout << fixed << setprecision(7) << showpoint;
	cout << r.num;
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