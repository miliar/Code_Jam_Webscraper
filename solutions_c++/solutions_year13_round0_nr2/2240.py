///*
// * p3.cpp
// *
// *  Created on: 2013-04-12
// *      Author: hpp3
// */
//#include <cmath>
//#include <iostream>
//#include <string>
//#include <vector>
//#include <fstream>
//#include <sstream>
//using namespace std;
//
//
//ofstream out("out.txt");
//
//bool isfair(int n) {
//	string s;
//	ostringstream convert;
//	convert << n;
//	s = convert.str();
//
//	for (int i = 0; i < s.length()/2; i++) {
//		if (s.at(i) != s.at(s.length()-i-1))
//			return false;
//	}
//	return true;
//}
//
//bool issquare(int n) {
//	int a;
//	a = sqrt(n);
//	return (a*a == n) and isfair(a);
//}
//
//bool isfairsquare(int n) {
//
//	return isfair(n) and issquare(n);
//
//}
//
//
//int main() {
//	ifstream f("input.txt");
//	int T;
//	f >> T;
//
//	for (int x = 0; x < T; x++) {
//		int a, b;
//		f >> a >> b;
//
//		int count = 0;
//
//		for (int n = a; n <= b; n++) {
//			count += isfairsquare(n);
//		}
//
//		out << "Case #" << x+1 << ": " << count << endl;
//	}
//
//
//
//	return 0;
//}
