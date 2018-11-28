#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int numInputs;
    cin >> numInputs;

    vector<int> digits;
    int n;

    for (int i = 1; i <= numInputs; i++) {
    	cin >> n;

    	if (n == 0) {
    		cout << "Case #" << i << ": INSOMNIA" << endl;
    		continue;
    	}
    	
    	int j = 1;
    	string num;

    	while (digits.size() != 10) {
    		num = to_string(n * j);
    		for (int k = 0; k < num.length(); k++) {
    			int newDigit = num[k] - '0';
    			
    			if (find(digits.begin(), digits.end(), newDigit) == digits.end()) {
    				digits.push_back(newDigit);
    			}
    		}
    		
    		j++;
    	}

    	cout << "Case #" << i << ": " << num << endl;
    	digits.clear();
    }

    return 0;
}