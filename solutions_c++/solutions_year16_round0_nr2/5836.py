/*
 * pancakes.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: Lesly
 */


#include <iostream>
#include <stack>
using namespace std;

void function1(int t)
{
	for (int i = 1; i <= t; i++){
		int count = 0;
		string s = "";
		cin >> s;

		int status = 0;
		int k = s.size();
		for(int j = k - 1; j >= 0; j--){
			if(status == 0 && s[j] == '-')
			{
				count++;
				status = 1;
			}
			else if(status == 1 && s[j] == '+')
			{
				count++;
				status = 2;
			}
			else if(status == 2 && s[j] == '-')
			{
				count++;
				status = 1;
			}
		}

		cout << "Case #" << i << ": " << count << endl;
	}
}


int main(){

	int t = 0;
	cin >> t;

	function1(t);


	return 0;
}

