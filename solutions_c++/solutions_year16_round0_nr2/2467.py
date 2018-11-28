#include <iostream>

using namespace std;


void conta(string entrada, int instancia){
	int i = 1;
	int cont = 0;
	char anterior = entrada[0];
	
	for(i = 1; i < entrada.length(); i ++){
		if(entrada[i] != anterior){
			cont ++;
		}
		anterior = entrada[i];
	}
	if(entrada[i-1] == '-'){
		cont++;
	}
	cout << "Case #"<< instancia << ": "<<cont<<endl;
}

int main(){
	int T;
	string entrada;
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> entrada;
		conta(entrada, i+1);
	}
}
