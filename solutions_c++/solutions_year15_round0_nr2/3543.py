#include <iostream>
#include <vector>
#define INF 1e9

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int t,d;
vi pla;

int main(){
	cin >> t;
	for(int cass = 1; cass <= t; ++cass){
		cin >> d;
		pla = vi(d);
		int maxim = 0;
		for(int i = 0; i < d; ++i){
			cin >> pla[i];
			if(pla[i] > maxim) maxim = pla[i];
		}
		int minim = INF;
		for(int i = 1; i <= maxim; ++i){
			int aux = i;
			for(int j = 0; j < d; ++j){
				aux += (pla[j]-1)/i;
			}
			if(aux < minim) minim = aux;
		}
		cout << "Case #" << cass << ": " << minim << endl;
	}
}