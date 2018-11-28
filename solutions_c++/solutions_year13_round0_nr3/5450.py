// Hedgemony.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cmath>
#include <cstddef>
#include <cstdlib>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <utility>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <iomanip>

using namespace std;

long long revnum(long long x){
	long long p = 0;
//	cout << "reversing " << x << endl;
	if(x%10 ==0)
		return 0;
	while(x > 0){
		p = p*10 + x%10;
		x = x/10;
	}
//	cout << "rev is " << p << endl;
	return p;
}

bool isPalin(long long x){
	ostringstream format_message(x);
	// ok: converts values to a string representation
	string a(format_message.str());
	string b(a);
	std::reverse(b.begin(),b.end());
	if(a==b){
		return true;
	}
	return false;
}

int _tmain(long long argc, _TCHAR* argv[])
{
	int T,t=0;
	cin >> T;
	vector<int> output(T,0);
	while(t<T){
		string strA, strB;
		long long A,B;
		cin >> A >> B;
		//A = stoi(strA);
		//B = stoi(strB);
		long long x = A;
		while(x <= B){
			//cout << "Solving " << x << endl;
			if(x == 2) {
				x++;
				continue;
			}
			if(x == 1){
				output[t]++;
				x++;
				continue;
			}
			if(!isPalin(x))
			{
				x++;
				continue;
			}
	//		cout << x << "is palin" << endl;
			/*if(!(x&(x-1))){
				x++;
				continue;
			}*/
	//		cout << x << "is square too !!" << endl;
			long long y = sqrt(x);
			if(y*y != x) {
				x++ ;
				continue;
			}
			if(isPalin(y)){
				output[t]++;
				//cout << y << " is palin too !! ---> result + 1" << endl;
			}
			x++;
		}
		t++;
	}
	for(int i = 0; i < T ; i++){
		cout << "Case #" << i+1 << ": " << output[i];
			cout << endl;
	}
	return 0;
}

