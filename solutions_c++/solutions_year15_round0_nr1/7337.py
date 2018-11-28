#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int proceso(vector<int> timidos){ 
	int cantAplaudiendo = timidos[0];
	int invito = 0;
	for (int i=1;i<timidos.size();++i){
		if (cantAplaudiendo<i){
			invito += (i-cantAplaudiendo);
			cantAplaudiendo += (i-cantAplaudiendo);
		}

		cantAplaudiendo += timidos[i];
	}
	return invito;
}

int main(){
	int ncas = 0;
	cin >> ncas;
	vector<int> timidos; 
	for (int cas = 1; cas < ncas + 1; cas++) { 
		cout << "Case #" << cas << ": "; 
		// Code here
			string value;
			timidos.clear();
			cin >> value;
			cin >> value;
			for (char v : value )
				timidos.push_back(v-'0'); 
			cout<<proceso(timidos);
		// End Code 

	cout << endl; }


	return 0;
}