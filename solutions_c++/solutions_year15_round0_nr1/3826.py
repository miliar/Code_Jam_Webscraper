#include <iostream>
#include <string>
#include <vector>
using namespace std;


int getcount(string &audiences) {
	vector<int> num(audiences.size(), 0);
	num[0] = audiences[0]-48;
	for(int i = 1; i < audiences.size(); i++) {
		num[i] = (audiences[i]-48) + num[i-1];
	}

	int max = 0;
	for(int i = 1; i < audiences.size(); i++) {
		int comp = i - num[i-1];
		if(comp > max){
			max = comp;
		}
	}
	return max;
}


int main() {
	int c;
	cin >> c;

	int n = c;
	while(c > 0) {
		int shyness;
		cin >> shyness;
		string audiences;
		getline(cin, audiences);
		audiences = audiences.substr(1);

		cout << "Case #" << n - c + 1 << ": " << getcount(audiences) << endl;
		c--;
	}
	return 0;
}
