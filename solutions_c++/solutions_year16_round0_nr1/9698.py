#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
int main(){
	optimizar_io
	int casos;
	cin >> casos;
	for(int ind = 1; ind <= casos; ind++){
		cout << "Case #" << ind << ": ";

		int n;
		cin >> n;
		if(n == 0){
			cout << "INSOMNIA\n";
			continue;
		}

		int copiaN = n;
		int contador = 0;
		vector<int> visitado(12);
		while(contador < 10){
			int actual = n;
			while(actual > 0){
				if(visitado[actual % 10] == 0){
					visitado[actual % 10]++;
					contador++;
				}
				actual /= 10;
			}
			if(contador == 10){
				cout << n << "\n";
				break;
			}
			n += copiaN;
		}
	}
	return 0;

}
