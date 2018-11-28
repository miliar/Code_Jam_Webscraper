#include <iostream>
using namespace std;

int T;
long long int N;
long long int tmp;
long long int contador;
bool digitos[10];
long long int visitados;
long long int pos;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	cin >> T;
	for(int i=1; i<=T; i++){
		cin >> N;
		if(N){
			contador = 1;
			visitados = 0;
			for(int i=0; i<=9; i++){
				digitos[i] = false;
			}
			while(true){
				tmp = N * contador;
				contador++;
				while(tmp){
					pos = tmp % 10;
					if(!digitos[pos]){
						digitos[pos] = true;
						visitados++;
					}
					tmp = tmp / 10;
					if(visitados == 10){
						break;
					}
				}
				if(visitados == 10){
					cout << "Case #" << i << ": " << N * (contador - 1) << "\n";
					break;
				}
			}
		} else {
			cout << "Case #" << i << ": INSOMNIA\n";
		}
	}
	return 0;
}