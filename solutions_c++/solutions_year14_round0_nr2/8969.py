// 	Cookie Clicker Alpha
//=======================================================================
//	John Rocamora
//	johnrocamora@gmail.com
//
//=======================================================================
// 	Problem
// 
// 		Start with 0 cookies
// 		Gain cookies at a rate of 2 cookies / second by clicking on a
//			giant cookie
//		Any time  you have at least C cookies, you can buy a cookie farm
//		Cookie farm
//			Costs C cookies
//			Gives you an extra F cookies per second
//		Once you have X cookies that you haven't spent on farms, you win!
//
//		Figure out how long it will take you to win if you use the best
//			strategy
//=======================================================================
//	Comments
//		
//		Cookies arrive continuously	USE DOUBLE
//
//		when should you buy a factory?
//			You can just use the initial rate to estimate how long it
//				will take 
//			Then whenever you reach the limit F, you have one extra
//				case to consider, it might take some time if we are
//				not careful
//		
//		Is there a way to optimize this with a formula?
//			Probably
//				I guess with a bit of basic calculus.
//
//		Ok, so looking at the slopes of numCurrentCookies, the best
//		solution is to 
//	
//		Ok, let's assume for now that we have two algorithms and check them
//			Linear All
//				The easiest case
//			Linear Last
//				The last part to reach the target is taken as a no buy
//				condition
//			Buy All
//				We always buy the cookie factory the moment we are able
//
//=======================================================================
//	Input
//
//		First Line: Number of test cases, T
//		Next Lines: C F X.
//			C	Cookies you have
//			F	Cookie rate
//			X	Cookie limit win
//
//
//	Output
//		
//		For each test case T output one line containing
//			"Case #x: y",
//				x	test case number
//				y 	minimum number of seconds it takes before X cookies
//		7 decimal places
//		
//	Limits
//
//		1 <= T <= 100
//
//=======================================================================


#include <stdio.h>
#include <iostream>
#include <algorithm>

// #define DEBUG_ON

#ifdef DEBUG_ON
#	define DEBUG(x) do { std::cerr << x; } while (0)
#else
#	define DEBUG(x) do {} while (0)
#endif


using namespace std;

// Function Prototypes

double timeBuyAll(double, double, double);

// Input variables
int numTestCases;
double C;
double F;
double X;

// Output 
double minTime;
double minTimeLinAll;
double minTimeBuyAll;
double minTimeBuyMostLinLast;
									
// Internal variables
int currTestCase;


int main()
{
	DEBUG("Problem B: Cookie Clicker" << endl);
	currTestCase = 0;

	// Read the file
	scanf("%d\n", &numTestCases);
	DEBUG("Number of test cases: " << numTestCases << endl);

	for (int k = 1; k <= numTestCases; k++) {

		currTestCase++;

		minTime = 0.0;
		
		// Get input
		scanf("%lf ", &C);
		scanf("%lf ", &F);
		scanf("%lf ", &X);
		scanf("\n");

		DEBUG("C = " << C << endl);
		DEBUG("F = " << F << endl);
		DEBUG("X = " << X << endl);

		// Solve problem
		//minTime = min(timeLinearAll(C, F, X), timeBuyAll(C, F, X));
		minTime = timeBuyAll(C, F, X);

		DEBUG("Case #" << currTestCase << ": " << minTime << endl);

		// Print result
		printf("Case #%d: %0.7lf\n", currTestCase, minTime);
		// cout << "Case #" << currTestCase << ": " << minTime << endl;
	}

	return 0;
}

double timeBuyAll(double C, double F, double X)
{
	double totalTime = 0.0;
	double risingTime = 0.0;
	double cookieTime = 0.0;
	double prevTotalTime;
	double index = 0.0;

	// If at any point prevTotalTime is smaller than the current,
	//		and larger or equal to 0 (to indicate more cases)
	//		break and return prevTotalTime

	risingTime = 0.0;
	cookieTime = X / (2.0 + 0.0 * F);
	totalTime = risingTime + cookieTime;

	while (1) {

		DEBUG(endl << index << endl);
		prevTotalTime = totalTime;
		DEBUG("Current prevTotalTime: " << prevTotalTime << endl);
		risingTime += C / (2.0 + index * F);
		DEBUG("Current risingTimeElement: " << C / (2.0 + index * F) << endl);
		DEBUG("Current risingTime: " << risingTime << endl);
		cookieTime = X / (2.0 + (index + 1) * F);
		DEBUG("Current cookieTime: " << cookieTime << endl);
		totalTime = risingTime + cookieTime;
		DEBUG("Current totalTime: " << totalTime << endl);

		if (prevTotalTime < totalTime) {
			DEBUG("Minimum Time: " << prevTotalTime << endl);
			return prevTotalTime;
		}
		
		index++;
	} 

	DEBUG("Minimum Time: " << totalTime << endl);
	
	return totalTime;
}
