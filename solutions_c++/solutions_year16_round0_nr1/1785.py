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

int main(){
	int T = in();
	for(int caso=1; caso<=T; ++caso){
		int N = in();
		cout << "Case #" << caso << ": ";
		if(N==0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		set<int> conj;
		int act = N;
		while(conj.size()!=10){
			stringstream ss;
			ss << act;
			string s = ss.str();
			for(int i=0;i<(int)s.size();i++)conj.insert(s[i]);
			act += N;
		}
		cout << act-N << endl;
	}
	return 0;
}
