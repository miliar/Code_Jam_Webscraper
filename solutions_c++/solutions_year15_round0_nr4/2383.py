#include<iostream>
using namespace std;

int main(){
	int T, x, r, c;
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> x >> r >> c;
		if((r*c)%x != 0){
			cout << "Case #" << t << ": RICHARD" << endl;
		}
		else{
			if(x==3 && r*c==3)cout << "Case #" << t << ": RICHARD" << endl;
			else if(x==4 && (r*c==4||r*c==8))cout << "Case #" << t << ": RICHARD" << endl;
			else if(x==1 || x==2) cout << "Case #" << t << ": GABRIEL" << endl;
			else cout << "Case #" << t << ": GABRIEL" << endl;
		}
	}
}
