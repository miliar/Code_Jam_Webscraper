#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <climits>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <stack>
#include <algorithm>
#include <queue>
#include <stdint.h>
using namespace std;
int main(){
	int T;
	cin >> T;
	string g;
	getline(cin,g);
	for(int t = 1; t <= T; t++){
		string s;
		getline(cin,s);
		printf("Case #%d: ",t);
		bool b = true;
		bool c;
		int count = 0;
		for(int i = s.size()-1; i >=0; i--){
			if(s[i]=='+')c = true;
			else c = false;
			if(c!=b){
				b=!b;
				count ++;
			}
		}
		cout << count << endl;
	}
	return 0;
}