#include <bits/stdc++.h>
using namespace std;

bool f2(int r, int c){		// true if richard wins
	if(r>c){int t=r; r=c; c=t;}
	if(c==1) return true;
	return false;
}

bool f3(int r, int c){
	if(r>c){int t=r; r=c; c=t;}
	if(r==1) return true;
	return false;
}

bool f4(int r, int c){
	if(r>c){int t=r; r=c; c=t;}
	if(r==1 || r==2) return true;
	return false;
}

int main(){
	int t, X, R, C; scanf("%d", &t);
	bool f;
	for(int v=0; v<t; v++){
		f = true;
		scanf("%d %d %d", &X, &R, &C);
		if(R*C%X!=0) {
			printf("Case #%d: RICHARD\n", v+1);
			continue;
		}
		switch(X){
			case 1: f = 0; break;
			case 2: f = f2(R, C); break;
			case 3: f = f3(R, C); break;
			case 4: f = f4(R, C); break;
		}
		if(f) printf("Case #%d: RICHARD\n", v+1); else printf("Case #%d: GABRIEL\n", v+1);
	}
}