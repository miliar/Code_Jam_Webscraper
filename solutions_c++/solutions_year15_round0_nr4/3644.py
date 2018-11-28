#include <iostream>
#include<stdio.h>
using namespace std;


int main() {

	int T,X,R,C;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&T);
	for(int i = 0; i < T; i++) {
		scanf("%d %d %d",&X,&R,&C);
		
		if((R*C) % X!=0) {
			cout << "Case #" << i+1 << ": RICHARD" << endl;
			continue;
		}
		if(X == 1 || X == 2) {
			cout << "Case #" << i+1 << ": GABRIEL" << endl;
			continue;
		}
		else if(X == 3){
			if(R*C == 6 || R*C == 9 || R*C == 12)
				cout << "Case #" << i+1 << ": GABRIEL" << endl;
			else
				cout << "Case #" << i+1 << ": RICHARD" << endl;
			continue;
		}
		else if(X == 4) {
			if(R*C == 16 || R*C == 12)
				cout << "Case #" << i+1 << ": GABRIEL" << endl;
			else
				cout << "Case #" << i+1 << ": RICHARD" << endl;
		}
	}

	return 0;
}
