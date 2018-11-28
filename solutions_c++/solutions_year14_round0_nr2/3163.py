#include <algorithm>
#include <cmath>
#include <cstdio>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

const int oo = 1000*1000*1000;

int nbTests;
double vitesse, previous, current;
double coutUpgrade, upgrade, but;

void computeAnswer()
{
	for(int iTest = 0; iTest < nbTests; ++iTest)
	{
		scanf("%lf%lf%lf", &coutUpgrade, &upgrade, &but);
		vitesse = 2;
		previous = oo;
		current = 0;
		while(current+but/vitesse < previous)
		{
			//printf("%lf\n", current);
			previous = current+but/vitesse;
			current += coutUpgrade/vitesse;
			vitesse += upgrade;
		}
		printf("Case #%d: %.7lf\n", iTest+1, previous);
	}
}

void readInput()
{
	//*
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	//*/
	scanf("%d", &nbTests);
}

int main()
{
	readInput();
	computeAnswer();
	return 0;
}
