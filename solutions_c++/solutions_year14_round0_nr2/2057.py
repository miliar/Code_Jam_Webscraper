#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <iomanip> // for output format

using namespace std;
int counter = 0;

double cookieSmall(double C, double F, double X) {
	// C is the cost for farm
	// F is the additional speed
	// X is the target
	// start with speed 2
	int k = 0; // the number of farms
	double total = 0;
	
	while ( C/(2 + k*F) +  X/(2 + k*F + F) <  X/(2 + k*F) ) {
		total += C/(2 + k*F);
		k += 1;
	}
	
	total += X/(2 + k*F);

	return total;
}


void process() {
	
	double first, second, third;
	cin >> first >> second >> third;

	// first = 3050.000;
	// second = 3.14159;
	// third = 99991.9990;
	
	double result = cookieSmall(first, second, third);
	cout << "Case #" << ++counter << ": " << setiosflags(ios::fixed) << 
		setprecision(7) << result << endl;
		
	return;
}


int main() {
	int t;
	scanf("%d", &t); // read the number of cases
	
	//t = 1;
	while (t--) {
		process();
	}

	return 0;
}