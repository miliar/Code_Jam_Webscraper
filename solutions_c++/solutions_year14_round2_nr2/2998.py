#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int cases;
	cin >> cases;
	for (int _ = 1; _ <= cases; _++){
		//cout << _ << endl;
		int a, b, k;
		cin >> a >> b >> k;
		int counter = 0;
		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++){
				//cout << (i&j) << endl;
				if((i&j) < k){
					counter++;
				}
			}
		}
		cout <<	"Case #" << _ <<": " << counter << endl;
	}
}