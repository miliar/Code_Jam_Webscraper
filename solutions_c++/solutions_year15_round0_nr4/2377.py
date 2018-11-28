#include <iostream>

using namespace std;


bool solve(){
	int x, r, c;
	cin>> x>> r>> c;
	if(c < r) swap(r, c);

	if(x > 4){
		cout<< "PARK"<< endl;
		return false;
	}

	if(x == 1){
		cout<< "GABRIEL"<< endl;
	}
	if(x == 2){
		if((r * c) % 2 != 0){
			cout<< "RICHARD"<< endl;
			return true;
		}
		if(r * c < 2){
			cout<< "RICHARD"<< endl;
			return true;
		}
		cout<< "GABRIEL"<< endl;
		return true;
	}
	if(x == 3){
		if((r * c) % 3 != 0){
			cout<< "RICHARD"<< endl;
			return true;
		}
		if(r < 2 || c < 3){
			cout<< "RICHARD"<< endl;
			return true;
		}
		cout<< "GABRIEL"<< endl;
		return true;
	}
	if(x == 4){
		if((r * c) % 4 != 0){
			cout<< "RICHARD"<< endl;
			return true;
		}
		if(r < 3 || c < 4){
			cout<< "RICHARD"<< endl;
			return true;
		}
		cout<< "GABRIEL"<< endl;
		return true;
	}

	return true;
}

int main(){
	cout.setf(ios::fixed); cout.precision(10);
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ": ";
		solve();
	}
	return 0;
}
