#include <iostream>
using namespace std;

int chartonum(char x){
	if (x=='0'){
		return 0;
	}
	if (x=='1'){
		return 1;
	}
	if (x=='2'){
		return 2;
	}
	if (x=='3'){
		return 3;
	}
	if (x=='4'){
		return 4;
	}
	if (x=='5'){
		return 5;
	}
	if (x=='6'){
		return 6;
	}
	if (x=='7'){
		return 7;
	}
	if (x=='8'){
		return 8;
	}
	if (x=='9'){
		return 9;
	}
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for (int j=0; j<t; j++){
		int n;
		cin>>n;
		n+=1;
		int a[n];
		char x;
		for (int i=0; i<n; i++){
			cin>>x;
			a[i]= chartonum(x);
		}
		int sofar= a[0], ans= 0, curr= 1;
		for (int i=1; i<n; i++){
			if (sofar>=i){
				sofar+=a[i];
			}
			else{
				ans+=i-sofar;
				sofar= i+a[i];
			}
		}
		cout<<"Case #"<<j+1<<": "<<ans<<endl;
		
	}
	
	return 0;
}