#include <iostream>

using namespace std;

double buildCount;
double cookiePerSecond;
double result;
double building;

void buildFunc(double C, double F, double X){

	result = building + X / cookiePerSecond; 

	building += C / cookiePerSecond;
	buildCount += 1.0;
	cookiePerSecond = 2.0 + (buildCount * F);

	if(result > building + X / cookiePerSecond){
		buildFunc(C, F, X);
	}
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(7);

	int T;

	cin >> T;

	for(int k = 1; k <= T; k++){
		double C;
		double F;
		double X;

		cin >> C >> F >> X;

		buildCount = 0.0;
		cookiePerSecond = 2.0;
		building = 0.0;

		buildFunc(C, F, X);

		cout << "Case #" << k << ": " << result << endl;
	}

	return 0;
}