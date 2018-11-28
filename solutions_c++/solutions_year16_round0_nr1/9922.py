#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <algorithm>
#include <map>
#include <fstream>
#include <bitset>
#include <cstring>
#include <utility>
#include <cstdlib>
#include <climits>
#include <ctime>
 
using namespace std;
 
int main(){
	ifstream file;
	ofstream output;
	output.open("Output");
	file.open("A-large.in");
	bitset<10> digits;
	int t, i = 1, count;
	long n, prod, current;
	file >> t;
	while(t){
		file >> n;
		if(!n)
			output << "Case #" << i << ": INSOMNIA" << endl;
		else{
			digits.reset();
			prod = count = 0;
			while(count != 10){
				prod += n;
				current = prod;
				while(current){
					if(digits[current % 10] == 0){
						digits[current % 10] = 1;
						++count;
					}
					current /= 10;
				}
			}
			output << "Case #" << i << ": " << prod << endl;
		}
		++i;
		--t;
	}
	return 0;
} 
