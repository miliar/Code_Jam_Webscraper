/*
 * main.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: cicy
 */

#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

bool checkFair(int x){
	vector<int> list;
	while(x>=10){
		list.push_back(x%10);
		x /= 10;
	}
	list.push_back(x);

	int first = 0, last = list.size()-1;
	while(first <= last){
		if(list.at(first++) != list.at(last--))
			return false;
	}
	return true;
}

bool checkSquare(int x){
	double d_sqrt = sqrt(x );
	int i_sqrt = d_sqrt;
	if ( d_sqrt == i_sqrt )
		return true;
	else
		return false;
}

int main(){
	int N;
	cin >> N;
	string line;
	getline(cin, line);

	for(int i=1; i<=N; i++){
		int count = 0;
		string line;
		getline(cin, line);
		istringstream iss( line );
		int first, last;
		iss >> first >> last;
		int a = ceil(sqrt(first)), b = sqrt(last);
		for(int i=a; i<=b; i++){
			if(checkFair(i) && checkFair(i*i)){
//				cout << i <<" ";
				count ++;
			}

		}
//		cout << tmp <<": " << checkFair(tmp) <<checkSquare(tmp) <<" ";
		cout << "Case #" << i << ": " <<count <<"\n";
		cin.clear();
	}

}


