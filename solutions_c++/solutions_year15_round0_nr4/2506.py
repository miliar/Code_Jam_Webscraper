#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
using namespace std;
int main(){
	FILE *fp, *ofp;
	freopen_s(&fp, "D-small-attempt0.in", "r", stdin);
	freopen_s(&ofp, "output.out", "w", stdout);
	int T = 0, conquer = 0;
	cin >> T;
	for (int k = 0; k < T; k++){
		int X, R, C;
		cin >> X >> R >> C;
		if (X == 1) conquer = 1;
		else if (X == 2){
			if (R == 1 && C == 2) conquer = 1;
			else if (R == 1 && C == 4) conquer = 1;
			else if (R == 2 && C == 1) conquer = 1;
			else if (R == 2 && C == 2) conquer = 1;
			else if (R == 2 && C == 3) conquer = 1;
			else if (R == 2 && C == 4) conquer = 1;
			else if (R == 3 && C == 2) conquer = 1;
			else if (R == 3 && C == 4) conquer = 1;
			else if (R == 4 && C == 1) conquer = 1;
			else if (R == 4 && C == 2) conquer = 1;
			else if (R == 4 && C == 3) conquer = 1;
			else if (R == 4 && C == 4) conquer = 1;
			else conquer = 0;
		}
		else if (X == 3){
			if (R == 2 && C == 3) conquer = 1;
			else if (R == 3 && C == 2) conquer = 1;
			else if (R == 3 && C == 3) conquer = 1;
			else if (R == 3 && C == 4) conquer = 1;
			else if (R == 4 && C == 3) conquer = 1;
			else if (R == 4 && C == 3) conquer = 1;
			else conquer = 0;
		}
		else if (X == 4){
			if (R == 3 && C == 4) conquer = 1;
			else if (R == 4 && C == 3) conquer = 1;
			else if (R == 4 && C == 4) conquer = 1;
			else conquer = 0;
		}
		if (conquer == 1) printf("Case #%d: GABRIEL\n", k + 1);
		else printf("Case #%d: RICHARD\n", k + 1);
	}
	return 0;
}