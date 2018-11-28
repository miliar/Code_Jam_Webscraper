#include <iostream>
#include <vector>
using namespace std;

vector<int> digitizer(int x){
	vector<int> returnValue;
	while(x>=10){
		returnValue.push_back(x%10);//take digit
		x=x/10; //or x/=10 if you like brevity
	}
	returnValue.push_back(x);
	return returnValue;
}

void counting_sheep(int n, int caseno){
	bool arr[10] = {false};
	vector<int> digits;
	int res, x = n;
	int truecount = 0, counter = 1;
	if (n == 0) {
		cout << "CASE #" << caseno << ": INSOMNIA" << endl;
		return;
	}
	while (truecount < 10) {
		digits = digitizer(x);
		for (int i = 0; i < digits.size(); i++){
			if (arr[digits[i]] == false){
				arr[digits[i]] = true;
				truecount++;
			}
		}
		res = x;
		counter++;
		x = n * counter;
		digits.clear();
	}
	cout << "CASE #" << caseno <<": "<< res << endl;

}
int main(int argc, char *argv[]) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tst, n;
	cin >> tst;
	for (int i = 0; i < tst;i++){
		cin >> n;
		counting_sheep(n, (i+1));
	}
}