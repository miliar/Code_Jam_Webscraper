#include <iostream>
#include <math.h>
using namespace std;

int factor(char num[], int N, int base){
	unsigned long long int numero=0;
	unsigned long long int mult=1;
	long long int fact=-1;
	for(int i=0;i<N;i++){
		numero+=(num[i]-'0')*mult;
		mult*=base;
	}
	int max=sqrt(numero)+1;
	for(int i=2;i<max;i++){
		if(numero%i==0){
			fact = i;
			break;
		}
	}
	return fact;
}

void aumentar(char num[],int N){
	int pos=1;
	while(true){
		if(num[pos]=='1'){
			num[pos]='0';
			pos++;
		}
		else{
			num[pos]='1';
			break;
		}
	}
}

int main(){
	int T,N,J,found;
	int divisores[10];
	char jamcoin[100];
	bool itWorks;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>N>>J;
		found=0;
		cout<<"Case #"<<i+1<<":"<<endl;
		jamcoin[0]='1';
		for(int j=1;j<N-1;j++) jamcoin[j]='0';
		jamcoin[N-1]='1';
		while(found<J){
			itWorks=true;
			for(int j=0;j<9;j++){
				int aux = factor(jamcoin,N,j+2);
				if(aux==-1){
					itWorks=false;
					break;
				}
				divisores[j]=aux;
			}
			if(itWorks){
				found++;
				for(int j=N-1;j>=0;j--) cout<<jamcoin[j];
				for(int j=0;j<9;j++) cout<<" "<<divisores[j];
				cout<<endl;
			}
			aumentar(jamcoin,N);
		}
	}
}
