#include <iostream>
using namespace std;

int analizar(int n,int numeros[]){
	int temp,numero;
	
	if(n==0) return 0;
	
	temp = n%10;
	numeros[temp]=1;
	
	analizar(n/10,numeros);
	
	
	return 1;
}

int main(int argc, char *argv[]) {
	int t,n,numeros[10],mult,resultado,temp;
	cin>>t;
	
	for(int i=0; i<t;i++){
		cin>>n;
		mult = 1;
		
		for(int j=0;j<10;j++){
			numeros[j]=0;
		}
		
		while(true){
			if(!analizar(n*mult,numeros)){
				resultado = 0;
				break;
			}
			for(int j=0;j<10;j++){
				if(numeros[j]==0){
					temp = 0;
					break;
				}
				else temp = 1;
			}
			if(temp == 1){
				resultado = n*mult;
				break;
			}
			mult++;
		}
		if(resultado==0)cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else cout<<"Case #"<<i+1<<": "<<resultado<<endl;
		
	}
	return 0;
}

