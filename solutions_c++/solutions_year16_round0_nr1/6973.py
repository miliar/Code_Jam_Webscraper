#include <stdio.h>
#include <string>
#include <iostream>
#include <bitset>
using namespace std;

void markDigits(long long i, std::bitset<10> &digits){
	if (i == 0){
		digits.reset(0);
		return;
	}

	while (i > 0){
		int temp = (int)i % 10;
		digits.reset(temp);
		i = i / 10;
	}
}

long long testForNum(int num){
	int i;
	std::bitset<10> digits;
	digits.set();
	for (i = 1; i < 75; i++){
		markDigits(num * i, digits);
		if (digits.none()){
			// *temp = i;
			return num * i;
		}
	}

	return -1;
}


int main(void) {
    /* number of test cases */
    unsigned int t;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
	int temp;
	cin>>temp;
	long long tempRes = testForNum(temp);
	if(tempRes == -1){
		cout << "Case #" << i << ": " << "INSOMNIA" << endl;
	}else{
	        cout << "Case #" << i << ": " << tempRes << endl;
	}
    }

    return 0;
}