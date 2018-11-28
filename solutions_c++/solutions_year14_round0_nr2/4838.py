#include <iostream>
#include <iomanip>
using namespace std;

float resolve_farming_tendencies(float c, float f, float x, float count) {
	float value1 = x / (2 + f*count);
	float value2 = c / (2 + f*count); 
	float value3 = x / (2 + f*(count+1));
	
	if(value1 > value2 + value3) {
		return resolve_farming_tendencies(c, f, x, count + 1) +  value2;
	} else {
		return value1;
	}
}

int main() {
	int tests, count;
	float c, f, x;
	float result;
	cout << std::fixed;
	
	cin >> tests;
	for(int ii = 1; ii < tests+1; ii++) {
		cin >> c;
		cin >> f;
		cin >> x;
		result = resolve_farming_tendencies(c, f, x, 0);
		cout << "Case #" << ii << ": " << std::setprecision(10) << result << endl;	
	}
	return 0;
}