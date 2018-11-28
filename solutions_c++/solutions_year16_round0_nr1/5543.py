#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include <fstream>

using namespace std;

set<int> addDigitsToSet(set<int> s, long val){	
	int dig;

	while(val >= 10) {
		dig = val%10;
		val = val/10;
		
		if(s.find(dig) == s.end()) {
			//cout << dig;
			s.insert(dig);
		}
	}
	
	if(s.find(val) == s.end()) {
		//cout << val;
		s.insert(val);
	}
	return s;
}

int returnNumber(long val){
	long i = 1;
	set<int> s;
	int newVal = val;

	if(val == 0) {
		return 0;
	}

	while(true){
		s = addDigitsToSet(s, newVal);
		if(s.size() == 10) {
			return newVal;
		} else {
			i = i +1;
			newVal = val * i;
		}
	}
}

int main(){
	int T;
	long val;

	ofstream myfile;
  	myfile.open ("example.txt");

	cin >> T;

	for(int i = 0; i<T; i++) {
		cin >> val;
		int y = returnNumber(val);
		if(y == 0) {
			myfile << "Case #" << i+1 << ": INSOMNIA" << endl;
		} else {
			myfile << "Case #" << i+1 << ": " << y << endl;
		}	
	}
	
  	myfile.close();
	return 0;
	
}
