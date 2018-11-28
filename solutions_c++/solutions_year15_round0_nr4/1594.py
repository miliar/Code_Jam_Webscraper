#include <bits/stdc++.h>
using namespace std;

int main(){
	int T; cin >> T;
	for (int t = 0; t < T; t++){
		int x, r, c; cin >> x >> r >> c;
		cout << "Case #" << t+1 << ": ";
		if (x==1) cout << "GABRIEL" << endl;
		else if (x==2){
			if ((r*c)%2==0) cout << "GABRIEL" << endl;
			else cout << "RICHARD" << endl;
		} else if (x==3){
			if ((r*c)%3==0 && min(r,c) >= 2) cout << "GABRIEL" << endl;
			else cout << "RICHARD" << endl;
		} else if (x==4){
			int a = min(r,c);
			int b = max(r,c);
			if (a>=3 && b==4) cout << "GABRIEL" << endl;
			else cout << "RICHARD" << endl;
		}
	}
	return 0;
} 
