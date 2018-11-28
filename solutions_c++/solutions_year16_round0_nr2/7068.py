#include<iostream>
using namespace std;
int getFlips(string s){
	int len = s.length();
	int counter = 0;
	char desired = '+';
	for (int i = len - 1; i >= 0; i--){
		char ch = s.at(i);
		while (i > 0){
			if (s.at(i - 1) == ch){
				i--;
			}
			else{
				break;
			}
		}

		if (ch != desired)
		{
			counter++;
			desired = desired == '+' ? '-' : '+';
		}
	}

	return counter;
}

int main(void) {
    /* number of test cases */
    unsigned int t;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
	string inputStr;
	cin>>inputStr;
        cout << "Case #" << i << ": " << getFlips(inputStr) << endl;
    }

    return 0;
}