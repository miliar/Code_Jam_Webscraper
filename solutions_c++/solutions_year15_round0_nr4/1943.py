#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <array>
#include <math.h>
#include <cmath>
#include <iomanip>

using namespace std;

#define For(i,m,n) for(int i=m; i<n; i++)


int main() {
	bool isSmall = true;
	if (isSmall) {
		//freopen("practice.txt","rt",stdin);
		freopen("D-small-attempt1.in","rt",stdin);
		freopen("D-small.out","wt",stdout);
	}
	else {
		freopen("D-large-practice.in","rt",stdin);
		freopen("D-large.out","wt",stdout);
	}
	
	int T;
	cin >> T;
	
	int X,R,C;
	string winner;
	string g = "GABRIEL";
	string r = "RICHARD";
	For(caseNum,1,T+1) {
		printf("Case #%d: ", caseNum);
		cin >> X >> R >> C;
		if (X == 1) winner = g;
		else if (X == 2 && (R*C)%2 == 0) winner = g;
		else if (X == 3 && (R*C)%3 == 0 && R > 1 && C > 1) winner = g;
		else if (X == 4 && (R*C)%4 == 0 && R > 2 && C > 2) winner = g;
		else winner = r;
		
		
		
		
		cout << winner << endl;
	}
	

	return 0;
	
}
