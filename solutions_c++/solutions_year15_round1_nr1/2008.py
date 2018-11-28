#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

#define OUTPUT_PREFIX "Case #"
#define INPUT_NAME "A-large.in"
#define OUTPUT_NAME "output.dat"

using namespace std;

long long firstM(int interval, int dish[]);
long long secondM(int interval, int dish[]);

int main() {

	ifstream input;
	ofstream output;

	int testcase;

	input.open(INPUT_NAME);
	output.open(OUTPUT_NAME);

	input >> testcase;

	for(int test=0;test<testcase;test++) {
		int interval;
		int dish[1000];

		input >> interval;

		for(int i=0;i<interval;i++) {
			input >> dish[i];
		}
		output << OUTPUT_PREFIX << test+1 << ": " << firstM(interval,dish) << " " << secondM(interval,dish) << endl;
	}

	return 0;
}

long long firstM(int interval, int dish[]) {
	long long ans=0;
	for(int i=1;i<interval;i++) {
		if(dish[i]<dish[i-1])
			ans+=(dish[i-1]-dish[i]);
	}
	return ans;
}

long long secondM(int interval, int dish[]) {
	long long ans=0;
	int mostEaten=0;
	for(int i=1;i<interval;i++) {
		if((dish[i-1]-dish[i])>mostEaten) mostEaten=dish[i-1]-dish[i];
	}
	for(int i=0;i<interval-1;i++) {
		if(dish[i]<mostEaten) {
			ans+=dish[i];
		} else {
			ans+=mostEaten;
		}
	}
	return ans;
}