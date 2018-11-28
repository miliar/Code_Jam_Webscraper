#include <iostream>
#include <cmath>
using namespace std;

int main (){
	int ncases;
	cin >> ncases;
	for(int i = 1; i <= ncases; i++){
		cout << "Case #" << i << ": ";
		int b;
		unsigned long long m;
		unsigned long long ml1;
		cin >> b >> m;
		ml1 = m - 1;
		if(pow(2,b-2) < m){
			cout << "IMPOSSIBLE" << endl;
		}else{
			cout << "POSSIBLE" << endl;
			for(int j = 0; j < b; j++){
				for(int k = 0; k < b; k++){
					if(k <= j){
						cout << "0";
					}else if(k == b-1){
						if(j == 0){
							cout << "1";
						}else{
							cout << ml1 % 2; ml1 /= 2;
						}
					}else{
						cout << "1";
					}
				}
				cout << endl;
			}
		}
	}
			

  
	return 0;
}


