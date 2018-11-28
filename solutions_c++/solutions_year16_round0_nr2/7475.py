// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <deque>
#include <vector>
#include <set>
#include <string>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0;
	string str;

	cin >> T;
	for(int t=0;t<T;t++){
		cin >> str;
		int k=0;
		for (std::string::reverse_iterator rit=str.rbegin(); rit!=str.rend(); ++rit){
			if(k%2==0){
				if(*rit=='-'){
					k++;
				}
			}else{
				if(*rit=='+'){
					k++;
				}
			}
		}
		cout << "Case #" << (t+1) << ": " << k << endl;
	}
	return 0;
}

