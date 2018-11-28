#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <math.h>
#include <map>

using namespace std;

int main(int argc, char** argv) {
	int T;
	cin >> T;

	double C, F, X;
	double R = 2.0;
	double currTime = 0.0;

	for(int i=1; i<=T; i++) {
		currTime = 0.0;
		R = 2.0;
		cin >> C;
		cin >> F;
		cin >> X;
		while(1) {
			double timeToXAfterFarm = C/R + X / (F + R);
			double timeToX = X / R;

			if(timeToXAfterFarm < timeToX) {
				currTime += C/R;
				R += F;
			} else {
				currTime += timeToX;
				break;
			}
		}
		cout << "Case #" << i << ": " << setprecision(19) << currTime << endl;
	}
}
