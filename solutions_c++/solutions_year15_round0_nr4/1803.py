#include <iostream>
using namespace std;

bool solve(int x,int r,int c){
	if(r > c)swap(r,c);
	if(x == 1){
		return true;
	}
	if(x == 2){
		if(((r*c)%2) == 0)return true;
	}
	if(x == 3){
		if(r == 2 && c == 3 || r == 3 && c == 3 || r == 3 && c == 4)return true;
	}
	if(x == 4){
		if(r == 3 && c == 4 || r == 4 && c == 4)return true;
	}
	return false;
}

int main(void){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		int x,r,c;
		cin >> x >> r >> c;
		cout << "Case #" << i+1 << ": " << (solve(x,r,c)?"GABRIEL":"RICHARD") << endl;
	}
	return 0;
}