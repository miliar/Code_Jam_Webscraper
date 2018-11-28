#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	
	int t,n,N,K,puntos;
	double aux;
	vector<double> piezasN, piezasK;
	cout.precision(8);
	cin.precision(6);
	cin >> t;
	for(int l = 1; l <= t; ++l){
		cout << "Case #" << l << ": ";
		cin >> n;
		piezasN.clear();
		piezasK.clear();
		for(int i = 0; i < n; ++i){
			cin >> aux;
			piezasN.push_back(aux);
		}
		for(int i = 0; i < n; ++i){
			cin >> aux;
			piezasK.push_back(aux);
		}
		sort(piezasN.begin(),piezasN.end());
		sort(piezasK.begin(),piezasK.end());

		N = K = puntos = 0;
		while(N<n){
			if(piezasN[N] > piezasK[K]){
				++puntos;
				++K;
			}
			++N;
		}
		cout <<  puntos << " ";


		N = K = 0;
		while(K<n){
			if(piezasN[N] < piezasK[K]){++N;}
			++K;
		}
		cout <<  (n-N) << endl;


	}

	return 0;
}