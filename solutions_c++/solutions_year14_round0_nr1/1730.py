#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int x = 0; x < t; x++){
		int a[17];
		for(int i = 0; i < 17; i++) a[i] = 0;
		for(int q = 0; q < 2; q++){
			int n, tp;
			cin >> n;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){ 
					cin >> tp;
					if(i == n-1){
						a[tp]++;
					}
				}
			}
		}
		int c = 0, p;
		for(int i = 1; i <= 16; i++){
			if(a[i] == 2){
				c++;
				p = i;
			}
		}
		cout << "Case #" << x+1 << ": ";
		if(c > 1){
			cout << "Bad magician!\n";
		}
		else if(c){
			cout << p << endl;
		}
		else
			cout << "Volunteer cheated!\n";
	}
	return 0;
}
