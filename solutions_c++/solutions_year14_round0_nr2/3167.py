#include <cstdio>
#include <vector>


void solve(int caseNo)
{
	double C, F, X;
	scanf ("%lf %lf %lf", &C, &F, &X);
	int n = X/C;
	//printf ("\n%lf %lf %lf %d", C, F, X, n);

	//initialize for zero cookie farms
	double rate = 2.0;
	double timeToBuyFarm = 0.0;
	double timeToGoal = X/rate;
	double totalTime = timeToGoal;
	double bestSoFar = totalTime;
	int i = 0;
	
	//maybe i should be initialized to 1
	while (i < n){
		timeToBuyFarm += C/rate;
		rate += F;
		timeToGoal = X/rate;
		totalTime = timeToBuyFarm + timeToGoal;
		if (bestSoFar > totalTime) bestSoFar = totalTime;
		//printf("\n%f", bestSoFar);
		i++;
	}
	if (caseNo > 1)
		printf("\n");
	printf("Case #%d: %.7lf", caseNo, bestSoFar);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
