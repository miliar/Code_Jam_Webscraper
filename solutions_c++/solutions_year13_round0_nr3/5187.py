/*
 * File:   main.cpp
 * Author: hawkwing
 *
 * Created on April 12, 2013, 7:21 PM
 */

#include <fstream>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

bool IsPalindrome(int num){
	stringstream ss;
	ss << num;
	string n=ss.str();
	for(int i=0;i<n.size()/2;i++){
		if(n[i]!=n[n.size()-i-1]){
			return false;
		}
	}
	return true;
}

int main(){
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	int T;
	in >> T;
	for(int i=0;i<T;i++){
		out << "Case #" << i+1 << ": ";
		int A,B;
		in >> A >> B;
		int fair_and_square=0;
		for(int j=ceil(sqrt(A));j<=floor(sqrt(B));j++){
			if(IsPalindrome(j) and IsPalindrome(pow(j,2))) fair_and_square+=1;
		}
		out << fair_and_square << endl;
	}
	return 0;
}