#include <stdio.h>

double czasDleFabryk(int ileFabryk, double c, double f, double x) {
	double czas = 0.0;
	double speed = 2.0;
	for(int i=1; i<=ileFabryk; i++ ) {
		czas += c/speed;
		speed += f;
	}
	czas += x/speed;
	return czas;
}

void testCase() {
	double c,f,x;
	scanf("%lf%lf%lf", &c, &f, &x);

	double bestTime = x/2.0;

	int ileFabryk = 1;
	while(true) {
		double currentTime = czasDleFabryk(ileFabryk++, c, f, x);
		if (currentTime < bestTime) {
			bestTime = currentTime;
		}
		else break;
	}
	printf("%.8f\n", bestTime);
}

int main()
{
	int testCases;
	scanf("%d", &testCases);

	for(int i=0; i<testCases; i++) {
		printf("Case #%d: ", i+1);
		fprintf(stderr, "Case #%d: ", i+1);
		testCase();
	}
	return 0;
}