#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

typedef unsigned int uint;

bool isPalindrome(uint n){
	uint rev=0, tmp=n;
	while(tmp != 0){
		rev *= 10;
		rev += tmp%10;
		tmp /= 10;
	}
	return n==rev;
}

int main(int argc, char *argv[]){
	string file;
	cout << "Filename: ";
	cin >> file;
	ifstream INPUT((file+".in").c_str());
	ofstream OUTPUT((file+".out").c_str());

	int limit;
	INPUT >> limit;
	for(int c=0; c<limit; c++){
		OUTPUT << "Case #" << (c+1) << ": ";
		long from, to;
		INPUT >> from;
		INPUT >> to;
		uint start = ceil(sqrt(from));
		uint end = floor(sqrt(to));
		int ret = 0;
		for(uint i=start; i<=end; i++){
			if (isPalindrome(i) && isPalindrome(i*i)) ret++;
		}
		OUTPUT << ret << endl;
	}

	OUTPUT.close();
	INPUT.close();
	return 0;
}
