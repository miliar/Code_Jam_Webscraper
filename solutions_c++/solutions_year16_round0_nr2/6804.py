#include "iostream"
#include "string"
using namespace std;

void flip(string& pancakes, int index) {
	for(int i=index; i>=0; --i) {
	    if(pancakes.at(i) == '-') pancakes.at(i) = '+';
	    else if(pancakes.at(i) == '+') pancakes.at(i) = '-';
	}
}

int main() {
	int T;
	cin >> T;
	string input;
	int ans[T];
	for(int i=0; i<T; ++i) {
	    cin >> input;
	    ans[i] = 0;

	    int index = input.length()-1; // bottom
	    while(index >= 0) {
	    	if(input.at(index) == '-') {
	    		flip(input, index);
	    		ans[i]++;
	    	}
	    	index--;
	    }
	}
	for(int i=0; i<T; ++i) {
		cout << "Case #" << i+1 << ": " << ans[i] << endl;
	}
	// End of Program //
		return 0;
}