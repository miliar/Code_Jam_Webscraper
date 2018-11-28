// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <deque>
#include <vector>
#include <set>
using namespace std;

void collect_digits(std::set<int>& digits, unsigned long num) {
    if (num > 9) {
        collect_digits(digits, num / 10);
    }
    digits.insert(num % 10);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0;
	unsigned long long N = 0;

	cin >> T;
	for(int t=0;t<T;t++){
		std::set<int> digits;
		cin >> N;
		if(N>0){
			for(unsigned long n=N;;n+=N){
				collect_digits(digits,n);
				if(digits.size()==10){
					cout << "Case #" << (t+1) << ": " << n << endl;
					break;
				}
			}
		}else{
			cout << "Case #" << (t+1) << ": INSOMNIA" << endl;
		}
	}
	return 0;
}

