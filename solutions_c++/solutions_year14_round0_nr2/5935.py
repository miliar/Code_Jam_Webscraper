#include <stdio.h>

int main() {
	FILE *inputFile, *outputFile;
	fopen_s(&inputFile, "B-large.in", "r");
	fopen_s(&outputFile, "BigSolutionB.txt", "w");

	int numberOfCases;
	fscanf_s(inputFile, "%i", &numberOfCases);

	double cookieFarmCost, extraCookies, cookiesGoal;
	for (int i = 0; i < numberOfCases; i++) {
		fscanf_s(inputFile, "%lf %lf %lf", &cookieFarmCost, &extraCookies, &cookiesGoal);
		double cookieRate = 2.0;
		double totalTime = 0;
		double leftoverCookies = cookiesGoal - cookieFarmCost;
		bool solved = false;

		if (leftoverCookies <= 0) {
			solved = true;
			totalTime += cookiesGoal / cookieRate;
		}

		while (!solved) {
			double currentRate = leftoverCookies / cookieRate;
			double futureRate = cookiesGoal / (cookieRate + extraCookies);

			if (currentRate < futureRate) {
				totalTime += cookiesGoal / cookieRate;
				solved = true;
				continue;
			}

			totalTime += cookieFarmCost / cookieRate;
			cookieRate += extraCookies;
		}

		fprintf_s(outputFile, "Case #%i: %.7f\n", (i+1), totalTime);

	}

	fclose(outputFile);
	fclose(inputFile);
}