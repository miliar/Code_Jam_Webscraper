#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <unordered_map>
using namespace std;

typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

Int A[1 << 12];
Int B[1 << 12];
Int T[1 << 12];

int SolveTest(int test){
	long double C, F, X;
	long double cps = 2;
	long double res = 0;
	long double timeToBuy;
	long double timeToFinishAfterBuy;
	long double timeToFinish;
	scanf("%Lf%Lf%Lf", &C, &F, &X);
	while(1){
		timeToBuy = C / cps;
		timeToFinishAfterBuy = timeToBuy + X / (cps + F);
		timeToFinish = X / cps;
		if(timeToFinishAfterBuy < timeToFinish){

			cps += F;
			res += timeToBuy;
			

		}
		else{
			res += timeToFinish;
			break;
		}



	}

	printf("Case #%d: %Lf\n", test + 1, res);
	return 0;
}


int main()
{
	freopen("blarge.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int T, t;
	char buf[1 << 7];
	gets(buf);
	sscanf(buf, "%d", &T);

	FOR(t, 0, T)
	{
		fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};