#include <iostream>
#include <algorithm>

using namespace std;

bool special_case(int O, int R, int C){

	if(R < C)
		swap(R, C);

	return O == 4 && R == 4 && C == 2;
}

int main(void){

	ios::sync_with_stdio(false);

	int T;
	int O, R, C;

	cin >> T;

	for(int k=1; k<=T; k++){

		cin >> O >> R >> C;

		cout << "Case #" << k << ": " << (O > max(R,C) || O > 2*min(R, C) || (R*C)%O || special_case(O, R, C) ? "RICHARD" : "GABRIEL") << endl;
	}

	return 0;
}
