//============================================================================
// Name        : fairandsquare.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <set>
using namespace std;
bool checkPalindrom(long long num){
	long long n = num;
	long long rev = 0;
	while(num >0){
		long long dig = num % 10;
		rev = rev *10 + dig;
		num = num /10;
	}
	return (n == rev);
}
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	ifstream in("small1.txt");
	ofstream out("small1.out");
	int cases;
	in >> cases;
	set<long long> s;
	long long zece = 10000001;
	for(long long i = 0; i <= zece; ++i){
		long long square = i*i;
		if(checkPalindrom(i) && checkPalindrom(square)){
			s.insert(square);
		}
	}
	for(int i = 1; i <= cases; i++){
		int a, b;
		in >>a >> b;
		long long count = 0;
		for(long long num = a; num <=b; ++num){
			if(s.count(num) == 1)
				count++;
		}
		cout <<"Case #" << i <<": " << count <<"\n";
		out << "Case #" << i <<": " << count;
		if(i != cases)
			out << "\n";
	}
	in.close();
	out.close();
	return 0;
}
