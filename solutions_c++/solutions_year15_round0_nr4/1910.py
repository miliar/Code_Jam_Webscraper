#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int CASE = 0;
string A = "RICHARD";
string B = "GABRIEL";
void judge(int x, int rr, int cc){
	int R = max(rr, cc);
	int C = min(rr, cc);

	cout << "Case #" << ++CASE << ": ";

	if( x == 1 )	cout << B << endl;
	else if( x == 2 ){
		if((R * C ) % 2 != 0)
			cout << A << endl;
		else
			cout << B << endl;
	}
	else if(x == 3){
		if( (R * C) % 3 != 0 )	
			cout << A << endl;
		else if(C == 1)
			cout << A << endl;
		else
			cout << B << endl;
	}
	else if(x == 4){
		if((R * C) % 4 != 0)
			cout << A << endl;
		else if( C < 3 )
			cout << A << endl;
		else
			cout << B << endl;	
	}
}

int main(){
	
	int T;
	cin >> T;
	while( T-- ){
		int x, r, c;
		cin >> x >> r >> c;
		judge(x, r, c);
	}

	return 0;
}
