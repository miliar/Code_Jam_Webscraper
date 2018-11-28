#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>


Federico Javier Pousa

void siguiente(string &s){
	for(int i=(int)s.size()-2; i>=0; i--){
		if(s[i]=='0'){
			s[i] = '1';
			return;
		}
		s[i] = '0';
	}
	return;
}

int main(){
	int N = 32;
	int J = 500;
	string act = "10000000000000000000000000000001";
	cout << "Case #1: " << endl;
	for(;J;){
		int cant1 = 0;
		int cant2 = 0;
		for(int i=0; i<(int)act.size(); ++i){
			if(act[i]!='1')continue;
			if(i%2==0){
				cant1++;
			}else{
				cant2++;
			}
		}
		bool sirve = true;
		sirve = sirve && ((cant1+cant2)%6==0);
		sirve = sirve && (abs(cant1-cant2)%6==0);
		if(sirve){
			J--;
			cout << act << " 3 2 3 2 7 2 3 2 3" << endl;
		}
		siguiente(act);
	}
	return 0;
}
