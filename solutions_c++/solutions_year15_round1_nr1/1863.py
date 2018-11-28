#include <iostream>
#include <vector>
using namespace std;

int metodo1(vector<int> &numeros){
	int acum=0;
	for(int j=0;j<numeros.size()-1;j++) { 
		if(numeros[j]-numeros[j+1]>0)
			acum+=numeros[j]-numeros[j+1];
	}
	return acum;
}
int metodo2(vector<int> &numeros){
	int maxdif=0;
	for(int j=0;j<numeros.size()-1;j++) { 
		if(numeros[j]-numeros[j+1]>maxdif)
			maxdif=numeros[j]-numeros[j+1];
	}
	int acum=0;
	for(int j=0;j<numeros.size()-1;j++) {
		if(numeros[j]-maxdif>0){
			acum+=maxdif;
		}
		else acum+=numeros[j];
	}
	return acum;
}
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {  
		int n;
		cin>>n;
		vector<int> numeros;
		for(int j=0;j<n;j++) { 
			int aux;
			cin>>aux;
			numeros.push_back(aux);
		}
		int m1=metodo1(numeros);
		int m2=metodo2(numeros);
		
		cout<<"Case #"<<i<<": "<<m1<<" "<<m2<<endl;
	}
	return 0;
}

