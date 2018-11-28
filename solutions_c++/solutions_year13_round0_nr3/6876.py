#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

bool fair(int n){
	int rev = 0; 
	int dig = 0;
	int num = n;
	while(num > 0){
		dig = num % 10;
		rev = rev * 10 + dig;
		num = num / 10;
	}
	return n == rev;
}

bool square(int n){
	if (n < 0){
		return false;
	}
	int r = (int)floor(sqrt(double(n)));
	if(fair(r)){
		return n == r*r;
	}
	return false;
}


int fair(int x, int y){
	int fairsquares = 0;
	for( ; x <= y; x++){
		if(square(x)){
			if(fair(x)){
				fairsquares++;
			}
		}
	}
	return fairsquares;
}

int main(){
	int ct = 0;
	int num, s, e;
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt0.in");
	fout.open("results.dat");
	if(!fin){
		cout << "File not found.";
		exit(1);
	}
	fin >> num;
	while(ct != num){
		fin >> s >> e;
		cout << "Case #" << ct+1 << ": " << fair(s, e) << "\n";
		fout << "Case #" << ct+1 << ": " << fair(s, e) << "\n";
		ct++;
	}
	return 0;
}

