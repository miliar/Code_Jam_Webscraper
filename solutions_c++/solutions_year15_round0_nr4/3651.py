#include "stdafx.h"
//#include <iostream>
//using namespace std;
//int main(){ 
//	
//	return 0;}
#include <iostream>
using namespace std;
int cs;
inline void o(bool Richard){
	if (Richard)printf("Case #%d: RICHARD\n", cs);
	else printf("Case #%d: GABRIEL\n", cs);
}
int main(){
	int T, x, r, c; cin >> T;
	for (cs = 1; cs <= T; cs++){
		cin >> x >> r >> c;
		if (x == 1){ o(0); continue; }
		if (r > c)swap(r, c);
		//make sure r<=c
		if (x == 4){
			if (c == 4 && (r == 3 || r == 4))
				o(0); else o(1); continue;
		}
		if (x == 2){
			if (r == 1 && c == 1 || r == 1 && c == 3 || r == 3 && c == 3){
				o(1); continue;
			}
			else{ o(0); continue; }
		}
		//x==3
		if (r == 2 && c == 3 || r == 3 && c == 3 || r == 3 && c == 4){
			o(0); continue;
		}
		else{ o(1); continue; }
	}
	return 0;
}