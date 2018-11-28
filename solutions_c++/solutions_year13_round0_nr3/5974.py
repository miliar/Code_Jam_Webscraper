#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

bool pal(int num) {
	vector<int> digits;

	while(true) {
		int a=num%10;
		digits.push_back(a);
		num=num/10;
		if(!num)
			break;
	}

	int s=digits.size();

	for(int i=0; i<s; i++) {
		if(digits[i]==digits.back()) {
			digits.pop_back();
		} else {
			break;
		}
		if(i==s-1)
			return true;
	}
	return false;
}

int main() {
    ofstream fout ("fair-square.out");
    ifstream fin ("fair-square.in");

    int numCases;
    fin >> numCases;

    for(int i=0; i<numCases; i++) {
    	int lower, upper, answer=0;
    	fin >> lower >> upper;

    	for(int j=lower; j<=upper; j++) {
    		if(pal(j)) {
    			double a=sqrt(j);
    			if((int)a!=a)
    				continue;
    			else if(pal((int)a))
    				answer++;
    		}
    	}

    	fout << "Case #" << i+1 << ": " << answer << "\n";
    }

    return 0;
}
