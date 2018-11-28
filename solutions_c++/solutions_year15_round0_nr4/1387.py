#include <iostream>

using namespace std;

void solve(int zap){
	cout << "Case #" << zap << ": ";
	int x,r,c;
	cin >> x >> r >> c;
	if(x==1){
		cout << "GABRIEL\n";
		return;
	}
	if(x==2){
		if(r*c%2)cout << "RICHARD\n";
		else cout << "GABRIEL\n";
		return;
	}
	if(x==3){
		if(r==1 || c==1 || r*c%3)cout << "RICHARD\n";
		else cout << "GABRIEL\n";
		return;
	}
	if(r*c>=12)cout << "GABRIEL\n";
	else cout << "RICHARD\n";
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)solve(i);
	return 0;
}
