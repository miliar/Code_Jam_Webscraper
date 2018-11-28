#include <iostream>
#include <vector>
using namespace std;

int main(){
	int T;
	int cas = 1;
	cin >> T;
	for(int w = 0; w < T; ++w){

		int r, aux;
		int num = 0;
		int trobat = 0; 
		vector <int> v(4);
		
		cin >> r;
		for(int i = 0; i < r-1; ++i) for(int k = 0; k < 4; ++k) cin >> aux;
		for(int k = 0; k < 4; ++k) cin >> v[k];
		for(int i = r; i < 4; ++i) for(int k = 0; k < 4; ++k) cin >> aux;
		
		cin >> r;
		for(int i = 0; i < r-1; ++i) for(int k = 0; k < 4; ++k) cin >> aux;
		for(int k = 0; k < 4; ++k) {
			cin >> aux;
			for(int t = 0; t < 4; ++t) 
				if(aux == v[t]) {
					++trobat;
					num = aux;
				}
		}
		for(int i = r; i < 4; ++i) for(int k = 0; k < 4; ++k) cin >> aux;
		
		cout << "Case #" << cas << ": ";
		if(trobat == 0) cout << "Volunteer cheated!" << endl;
		else if(trobat == 1) cout << num << endl;
		else cout << "Bad magician!" << endl;
		++cas;
	}
	
}