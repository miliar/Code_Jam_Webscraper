#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

void count_one(int number, set<int> * mySet) {
	//cerr << "number is " << number << endl;
	while(number >= 1) {
		int digit = number % 10;
	//	cerr << "digit is " << digit << endl;
		mySet->insert(digit);
		number /= 10;
	}
}

void count(int number) {
	int copy = number;
	set<int> * mySet = new set<int>;
	if(number == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}
	while(mySet->size() != 10) {
	//	cerr << "set size is " << mySet->size() << endl;
		count_one(copy,mySet);
		copy += number;
	}
	cout << copy - number << endl;
}

int main() {
	string line;
	int testNum;
	getline(cin, line);
	stringstream ss(line);
	ss >> testNum;
	int ct = 1;
	while(testNum > 0) {
		int number;
		getline(cin, line);
		stringstream num(line);
		num >> number;
		cout << "Case #" << ct << ": ";
		count(number);
		testNum--;
		ct++;
	}
	return 0;
}