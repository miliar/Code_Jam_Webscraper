using namespace std;
#include <iostream>

int main(){
	
	int T;
	cin >> T;
	for (int n = 1; n <= T; n++){
		int Smax;
		cin >> Smax;
		int count = 0;
		int invitar = 0;
		for (int i = 0; i <= Smax; i++){
			int aux;
			char c;
			cin >> c;
			aux = (int)(c-'0');
			if (aux && count < i){
				invitar += (i - count);
				count = i;
			}
			count += aux;
		}
		cout << "Case #" << n << ": " << invitar << endl;
	}
	
}
