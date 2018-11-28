#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int nbTests;
	scanf("%d", &nbTests);
	for (int testNb = 1; testNb <= nbTests; testNb++){
		int X, R, C;
		scanf("%d%d%d", &X, &R, &C);
		
		if(X == 1){
			cout << "Case #" << testNb << ": GABRIEL\n";
			continue;
		}
		if(X >= 7){ //polyomino met gat int midden
			cout << "Case #" << testNb << ": RICHARD\n";
			continue;
		}
		if((R*C) % X != 0){
			cout << "Case #" << testNb << ": RICHARD\n";
			continue;
		}
		
		if(X == 2){ //implied by previous if that there is an even number of squares
			cout << "Case #" << testNb << ": GABRIEL\n";
			continue;
		}
		
		//hardcoded
		//R <= C
		int Rt = min(R,C);
		C = max(R,C);
		R = Rt;
		
		if(X == 3){
			//possibilities: 1x3 2x3 3x3 3x4 
			if(R == 1){ //pick L
				cout << "Case #" << testNb << ": RICHARD\n";
				continue;
			}
			else{
				cout << "Case #" << testNb << ": GABRIEL\n";
				continue;
			}
		}
		
		if(X == 4){
			//possibilities: 1x4 2x4 3x4 4x4 2x2
			if(R == 2 && C == 2){ //pick I
				cout << "Case #" << testNb << ": RICHARD\n";
				continue;
			}
			if(R == 1 && C == 4){ //pick O
				cout << "Case #" << testNb << ": RICHARD\n";
				continue;
			}
			if(R == 2 && C == 4){ //pick squiggly
				cout << "Case #" << testNb << ": RICHARD\n";
				continue;
			}
			if((R == 3 || R == 4) && C == 4){
				cout << "Case #" << testNb << ": GABRIEL\n";
				continue;
			}
		}
	}
	return 0;
}