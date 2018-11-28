#include <iostream>

using namespace std;

bool dig[10];

bool counted_all(){
	for(unsigned int i = 0; i < 10; i++){
		if(dig[i] == false) return true;
	}
	return false;
}

int main(){
	int t,n,n1,nbase,i,j=1;
	bool b;
	cin >> t;
	while(t--){
		i=1;
		for(unsigned int k = 0; k < 10; k++) dig[k] = false;
		cin >> n;
		nbase = n;
		cout << "Case #" << j++ << ": ";
		do{
			n1=n;
			// cout << n << endl;
			if(n == 0) {
				cout << "INSOMNIA";
				break;
			}
			while(n1 > 0){
				// cout << n1 << endl;
				dig[n1%10] = true;
				n1/=10;
			}
			n=nbase*++i;
		} while ( counted_all() );
		if(n != 0) cout << nbase*(i-1) << endl;
		else cout << endl;
	} 	
	return 0;
}