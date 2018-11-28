#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <vector>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

const char* inputFile  = "B-large.in";
const char* outputFile = "B-large.out";

class Solver
{
public:
	pair<int, int> solveTest(int N, long long P, long long& maxG, long long& maxP)
	{
    maxG = 0;
    maxP = 0;
    long long size = 1ll << N;
    long long grab = size / 2;
    long long point = grab;
    int steps = 0;
    while (P > point && steps < N)
    {
      steps++;
      grab /= 2;
      point += grab;
    }
    maxG = min((1ll << (steps + 1)) - 2, size - 1);

    steps = 0;
    point = 1;
    grab = 1;
    while (point + grab <= P)
    {
      steps++;
      point += grab;
      grab *= 2;
    }
    steps = N - steps;
    maxP = size - (1ll << steps);
	}
};

int main()
{
	freopen(inputFile, "r", stdin);
	freopen(outputFile, "w", stdout);
	int T;
	scanf("%d", &T);

	Solver solver;
	for (int testNumber = 1; testNumber <= T; ++testNumber)
	{
    int N;
    long long P;
    cin >> N >> P;
    long long maxG, maxP;
    solver.solveTest(N, P, maxG, maxP);
		printf("Case #%d: ", testNumber);
    cout << maxG << " " << maxP << endl;
	}
	return 0;
}
