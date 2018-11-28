#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int lastNumber(int n){
	if(n == 0) return -1;

	int digitToCheck = 10;
	vector<bool> digits;
	for(int i = 0; i < 10; ++i){
		digits.push_back(true);
	}
	int sum = n;
	
	while(digitToCheck){
		int temp = sum;

		while(temp > 0){
			int digit = temp %10;
			if(digits[digit]){
				digits[digit] = false;
				digitToCheck--;
			}
			temp /= 10;
		}
		sum += n;
	}

	return sum - n;
}

int main() {
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    int lastNum = lastNumber(n);
    cout << "Case #" << i << ": ";
    if(lastNum!= -1){
    	cout << lastNum;
    } else{
    	cout << "Insomnia";
    }

    cout << endl;
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
