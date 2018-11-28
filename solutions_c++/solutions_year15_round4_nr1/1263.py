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
	int T, R, C;
	cin >> T;
	for(int caso=1; caso<=T; ++caso){
		bool sirve = true;
		cin >> R >> C;
		int mini = 0;
		vector<string> b;
		string aux;
		for(int i=0; i<R; ++i){
			cin >> aux;
			b.push_back(aux);
		}
		for(int i=0; i<R; ++i){
			for(int j=0; j<C; ++j){
				if(b[i][j]=='.')continue;
				int der = 0;
				for(int k=j+1; k<C; ++k){
					if(b[i][k]!='.'){
						der = 1;
						break;
					}
				}
				int izq = 0;
				for(int k=j-1; k>=0; k--){
					if(b[i][k]!='.'){
						izq = 1;
						break;
					}
				}
				int up = 0;
				for(int k=i-1; k>=0; k--){
					//~ cerr << "k: " << k << endl;
					if(b[k][j]!='.'){
						up = 1;
						break;
					}
				}
				int down = 0;
				for(int k=i+1; k<R; ++k){
					if(b[k][j]!='.'){
						down = 1;
					}
				}
				if(down+up+der+izq==0){
					sirve = false;
				}
				if(b[i][j]=='^'){
					//~ cerr << up << endl;
					if(!up)mini++;
				}
				if(b[i][j]=='v'){
					if(!down)mini++;
				}
				if(b[i][j]=='>'){
					if(!der)mini++;
				}
				if(b[i][j]=='<'){
					if(!izq)mini++;
				}
			}
		}
		
		if(!sirve){
			cout << "Case #" << caso << ": IMPOSSIBLE" << endl;
		}else{
			cout << "Case #" << caso << ": " << mini << endl;
		}
		
	}
	
	
	return 0;
}



