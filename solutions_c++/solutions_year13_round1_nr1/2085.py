#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

#define all(c) c.begin(), c.end()


using namespace std;
long int t, r;
long int black;
const double PI = 3.1415926;

bool paintUsed(){
	/*
	double i = PI * pow(r,2);
	double j = PI * pow(r+1, 2);
	double left = t - (j-i)/PI;
	*/
	long int i = pow(r,2);
		long int j = pow(r+1, 2);
		long int left = t - (j-i);
	//cout << left << endl;
	//cout << i << " " << j << " " << endl;
	if(left>=0) {
		t = left;
		black++;
		r = r+2;
		return true;
	}else {
		return false;
	}

}

int draw(){
	while(paintUsed()){
	//	r = r+ 2;
	}
	return black;
}


int run(){
	cin >> r >> t;
	black = 0;

	draw();

	return black;
}

int main(){
	int T;
	cin >> T;
	for (int t = 0; t< T; t++){
	cout << "Case #" << t+1 << ": " << run() << endl;
	}
	return 0;
}
