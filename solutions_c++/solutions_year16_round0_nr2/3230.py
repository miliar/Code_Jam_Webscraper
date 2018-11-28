#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int T;
    cin >> T;
    string pancakes;
    getline (cin, pancakes);
    for (auto t = 0; t < T; t ++) {
	getline (cin, pancakes);
	
	vector<int> flips_pos(pancakes.size()); // number of flips needed to get all to be positive.
	vector<int> flips_neg(pancakes.size()); // number of flips needed to get all to be negative. 
	if (pancakes[0] == '+') {
	  flips_pos[0] = 0;
	  flips_neg[0] = 1;
	}
	else { // it is '-'
	  flips_pos[0] = 1;
	  flips_neg[0] = 0;
	}
	
	
	for (auto i = 1; i < pancakes.size(); i ++) {
	    // if the current one is positive, pos is equal to the number of pos before it. 
	    if (pancakes[i] == '+') {
		flips_pos[i] = min(flips_pos[i - 1], 
				   flips_neg[i - 1] + 1); 
		flips_neg[i] = min(flips_pos[i - 1] + 1, // flip all to '-'
				   flips_neg[i - 1] + 2); // first flip the prev '-' to '+', then flip all to '-'
		
	    }
	    if (pancakes[i] == '-') {
		flips_neg[i] = min(flips_pos[i - 1] + 1, // flip prev '+' to '-'
				   flips_neg[i - 1]); 
		flips_pos[i] = min(flips_pos[i - 1] + 2, // flip prev '+' to '-', then flip all to '+'
				   flips_neg[i - 1] + 1); // flip all to '+;
	    }
	}
	cout << "Case #" << t + 1 << ": " << min(flips_pos[pancakes.size() - 1], flips_neg[pancakes.size() - 1] + 1) << endl; 
    }
}
