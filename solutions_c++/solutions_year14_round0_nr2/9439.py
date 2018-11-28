#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
using namespace std;

#define FOR(i, a, n) for((i)=0;(i)<(int)(n);(i)++)
#define MIN(a,b) (((a)<(b))?(a):(b))

int i, j, k, n, in;
char c;

double current_rate, current_coin;
double C, F, X;

template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}

void getinput()
{
	scanf("%lf %lf %lf", &C, &F, &X);
}

void init()
{
	current_rate = 2.0;
	current_coin = 0;
}

double calcTime(double cr)
{
	return X/cr;
}

double r_calculate(double cr)
{
	if (calcTime(cr) < C/cr + calcTime(cr+F))
	{
		return calcTime(cr);
	}
	else
	{
		return C/cr +  r_calculate(cr+F);
	}
}

double calculate()
{
	return r_calculate(current_rate);
}

void output(int case_no)
{
	printf("Case #%d: ", case_no+1);
	
	printf("%.7lf", calculate());	
	
	printf("\n");
}

void main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt","w",stdout);

	scanf("%d", &n);

	FOR(in, 0, n)
	{
		init();
		getinput();
		calculate();
		output(in);
	}
}