#include <iostream>

using namespace std;

int T,x,r,c;

int main(){
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		cin >> x>>r>>c;
		if (r>c) swap(r,c);
		cout << "Case #"<<ti<<": ";
		if (r*c<x || r*c%x!=0){
			cout <<"RICHARD"<<endl;
			continue;
		}
		if (x<=2){
			cout << "GABRIEL"<<endl;
		}
		if (x==3){
			if (r==3 || (r==2 && c==3)) cout << "GABRIEL"<<endl;
				else cout<<"RICHARD"<<endl;
		}
		if (x==4){
			if (r>=3 && c>=4) cout << "GABRIEL"<<endl;
				else cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}
