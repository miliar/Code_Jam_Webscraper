#include <iostream>
using namespace std;

int main() {
	int cases = 0;
	cin >> cases;
	for(int c=0;c<cases;c++){
		int a = 0;
		int b = 0;
		cin >> a;
		cin.get();
		cin >> b;
		int denom=1, num=2, gen=0; 
		while(denom<b){
			denom *= 2;
			gen += 1;
		}
		while(num<a){
			num *= 2;
			gen -= 1;
		}
		if(denom != b){
			cout<<"Case #"<<c+1<<": impossible";
		}
		else{
			cout<<"Case #"<<c+1<<": "<<gen;
		}
		cout << endl;
	}
	return 0;
}