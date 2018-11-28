//Qualification Round 2015
//Irvin Gonzalez


#include <iostream>
#include <utility>
#include <vector>
#include <string>

void solve_it(std::istream& cin, std::ostream& cout) {
	//stuff happens here 
	int max;
	cin >> max;
	
	std::string aud;
	cin >> aud;

	int count = 0;
	int friends = 0;
	for(int i =0; i <= max; i++) {
		int shy = aud[i] - '0';
		if(shy > 0){
			if(count < i) {
				friends +=(i-count);
				count += (i-count); } }
		count += shy; }

	cout << friends;

}

int main() {
	using namespace std;
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++) {
		cout << "Case #" << i+1 << ": ";

		solve_it(cin, cout);

		cout << endl; }
}
