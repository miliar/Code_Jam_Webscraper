#include <iostream>
#include <vector>

double checkTime(double c, double f, double x, double timeSoFar, double currentF, double lastTime)
  {
		double timeToGoal = x / currentF; //withoutExtraFarm
		double timeToNextFarm = c / currentF;
		double totalTime = timeSoFar + timeToGoal;
		if (totalTime > lastTime) return lastTime;
		
		return checkTime(c, f, x, timeSoFar + timeToNextFarm, currentF + f, totalTime);
	
}

void solvecase(int caseNumber)
{
	double c, f, x; scanf_s("%lf %lf %lf", &c, &f, &x);
 	printf(" %.7f", checkTime(c, f, x , 0 , 2, x/2));
}


int main() {
	int t; scanf_s("%d", &t);
	int counter = 0;
	while (t--)
	{
		printf("CASE #%d: ", ++counter);
		solvecase(counter);
		printf("\n");
	}
	return 0;
}