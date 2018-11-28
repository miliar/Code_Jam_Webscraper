// by Naciraa
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


using namespace std;

int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}


int main(){
	int cases;
	cin >> cases;
	string res;
	for(int caso=1; caso<=cases; ++caso){
		int x,r,c;
		cin >> x >> r >> c;
		if(r > c){
			swap(r,c);
		}
		if(x == 1){
			res = "GABRIEL";
		}
		if(x == 2){
			if((r*c) % 2 == 0 ){
				res = "GABRIEL";
			}else{
				res = "RICHARD";
			}
		}
		
		if (x == 3){
			if(((r == 2) && (c == 3))||((r == 3) && (c == 3))||((r == 3) && (c == 4))){
				res = "GABRIEL";
			}else{
				res = "RICHARD";
			}
			
		}
		if (x == 4){
			if(((r == 3) && (c == 4))||((r == 4) && (c == 4))){
				res = "GABRIEL";
			}else{
				res = "RICHARD";
			}
			
		}
		
		cout << "Case #" << caso <<": " << res << endl;
	}

return 0;
}

