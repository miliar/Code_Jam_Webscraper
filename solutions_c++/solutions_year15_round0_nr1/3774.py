/*
 * a.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: dimalit
 */

#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int a_solve(const string& s){
	int Smax = s.length() - 1;
	int *arr = new int[Smax+1];
	for(int i=0; i<=Smax; i++)
		arr[i] = s[i]-'0';

	int stood = 0;
	int friends = 0;
	int shy = 0;

	for(;;){
		// 1 raise who can
		for(;shy<=stood && shy<=Smax; shy++)
			stood += arr[shy];
		// 2 exit if ok
		if(shy > Smax)
			break;
		// 3 add friends
		int need = shy - stood;
		friends += need;
		stood += need;
	}// main loop

	delete arr;
	return friends;
}

int main(){

	freopen("a.in", "rb", stdin);
	freopen("a_large.out", "wb", stdout);

	int T;
	cin >> T;

	for(int t=0; t<T; t++){
		int Smax;
		cin >> Smax;
		string s;
		cin >> s;

		int res = a_solve(s);
		cout << "Case #" << (t+1) << ": " << res << endl;
	}

	return 0;
}


