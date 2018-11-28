/*
 * FourthQrFifteen.cpp
 *
 *  Created on: 11 kwi 2015
 *      Author: KAMIL
 */
#include <iostream>
#include <cstdlib>
#include <list>
#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

bool solve(int x, int r, int c){
	if(x > 2 && (r == 1 || c == 1))
			return false;
	if(x==4 && (r==2 || c==2))
			return false;
	if((r*c)%x != 0)
		return false;
	return true;
}


int main(){
	int testNum;
	int * x;
	int * r;
	int * c;

	cin >> testNum;
	x = new int[testNum];
	r = new int[testNum];
	c = new int[testNum];

	for(int i=0; i<testNum; i++){
		cin>>x[i];
		cin>>r[i];
		cin>>c[i];
	}


	for(int i=0; i<testNum; i++){
		cout << "Case #" << (i+1) << ": ";
		if(solve(x[i], r[i], c[i]))
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}

return 0;
}
