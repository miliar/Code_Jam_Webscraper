#include <iostream>
#include <vector>

using namespace std;
int process(string n) {
	int idx = 0;
	int count = 0;
	string final = "";
	for (int i = 0; i < n.length(); i++) {
		final += "+";
	}
	//cout << final << endl;
	if ( n == final)
		return 0;
	size_t f_plus_found = 0;
	size_t f_minus_found = 0;
	size_t last_minus = 0;
	int ctr = 0;
	while(1) {
		
		if (n[0] == '+') {
			if (n.find("-") != string::npos) {
				f_minus_found = n.find("-");
				
			}
		} else {
			if (n.find("+") != string::npos) {
				f_plus_found = n.find("+");
				
			} else {
				last_minus = n.find_last_of("-");
			}
			//cout << "last " << last_minus << endl;
		}
		if ( f_plus_found != string::npos && (f_plus_found > 0)) {
			for (int i = 0; i < f_plus_found; i++) {
				n[i] = '+';
			}
			f_plus_found = string::npos;
		} else if (f_minus_found > 0 && f_minus_found != string::npos) {
			for (int i = 0; i < f_minus_found; i++) {
				n[i] = '-';
			}
			f_minus_found = string::npos;
		} else if (last_minus > 0 || last_minus == 0) {
			
			for (int i = 0; i < last_minus + 1; i++) {
				n[i] = '+';
			}
		}
		//cout << " final " << final << " iter " << n << endl;
		//cout << f_plus_found << " " << f_minus_found << endl;
		count++;
		ctr++;
		if (n == final) break;
	}
	return count;
}
int main() {
	int N;
	scanf("%d", &N);
	int cases = 0;
	while (N--) {
		cases++;
		string number;
		cin >> number;
		int ret = process(number);
		printf("Case #%d: %d\n", cases, ret);
	}
	return 0;
}