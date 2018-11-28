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

int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

string flip(string s, int i){
	string res = s;
	for(int j=0; j<=i; ++j){
		if(s[j]=='+'){
			res[i-j] = '-';
		}else{
			res[i-j] = '+';
		}
	}
	return res;
}

int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; ++caso){
		string s;
		cin >> s;
		int fin = s.size()-1;
		int res = 0;
		while(fin!=-1){
			while(fin>=0&&s[fin]=='+')fin--;
			if(fin==-1)break;
			int mas = 0;
			for(int i=0; i<(int)s.size(); ++i){
				if(s[i]=='-')break;
				mas++;
			}
			if(mas){
				s = flip(s, mas-1);
				res++;
			}
			int menos = 0;
			for(int i=0; i<(int)s.size(); ++i){
				if(s[i]=='+')break;
				menos++;
			}
			if(menos){
				s = flip(s, menos-1);
				res++;
			}
		}
		cout << "Case #" << caso << ": " << res << endl;
	}
	
	return 0;
}
