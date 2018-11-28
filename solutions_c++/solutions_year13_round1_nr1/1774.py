#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <math.h>
using namespace std;

long long bulleye(){
	long long r,t;
	cin >> r >> t;

	long long firstRing = 2*(r+1) -1;
	long long count = 0;
	long long test  = firstRing;
	while(test<=t){
		count++;
		t -= test;
		test += 4;
	}
	
	return count;
}

int main(){
	ifstream input("A-small-attempt1.in");
	cin.rdbuf(input.rdbuf());

	ofstream output("small.txt");
	cout.rdbuf(output.rdbuf());
	
	int T;
	cin >> T;

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": " << bulleye() << endl;
	}
	
	return 0;
}