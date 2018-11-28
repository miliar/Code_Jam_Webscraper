#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;
		

bool umoudois(long long n) {
	stringstream ss;
	ss << n;
	string str = ss.str();
	long long size = str.size();
	for(long long i=0; i< size ; i++) {
		if(str[i] > 2+48) return false;
	}
	return true;
}

bool palindrome(long long n) {
	stringstream ss;
	ss << n;
	string str = ss.str();
	long long size = str.size();
	bool pal=true;
	for(long long i=0; i< size ; i++) {
		if(str[i] != str[size-1-i]) { pal=false; break; }
	}
	return pal;
}
		
int contadig(int n) {
	if(n/10 ==0) return 1;
	int i=0;
	while(n > 0) {
		n=n/ 10;
		i++;
	}
	return i;
}
		
int main() {
	long long i=1;
	
	int T;
	int C=1;
	cin >> T;
	
	while(T-- >0 ) {
		long long resp=0;
		
		int a, b;
		cin >> a >> b;
		
		for(int i=sqrt(a); i<=sqrt(b)+1; i++) {
			long long quad = i*i;
			if(quad >= a && quad <= b && palindrome(i) && palindrome(quad)) resp++;
		}
		
		cout << "Case #"<<C++<<": "<<resp<<endl;
	}	
	//int digitos = contadig(i);
	//if(digitos %2 == 0 && umoudois(i) && palindrome(i) && palindrome(i*i)) cout << digitos << "	" << i << "		" << endl;
	
}

