#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define L 101 

bool Desacomodado(char pan[],int lpan){
	int i=0;
	bool desac=false;
	while(desac==0 && i<lpan){
		if(pan[i]=='-') desac=true;
		i++;
	}
	return desac;
}
void RealizarMetodo(char pan[],int lpan){
	int i=0,j=0;
	char aux[L];
	bool enc=false;
	while(i<lpan && enc==false){
		if(pan[i]!=pan[i+1]) enc=true;
		i++;
	}
	for(;j<i;j++){
		if(pan[j]=='-') aux[j]='+';
		else aux[j]='-';
	}
	for(i=0,j--;j>=0;j--,i++){
		pan[i]=aux[j];
	}
	
}
int CantMan(char pan[],int lpan){
	int cant=0;
	while(Desacomodado(pan,lpan)){
	RealizarMetodo(pan,lpan);
	cant++;
	}
	
	return cant;
}

int main(int argc, char *argv[]) {
	char pan[L];
	int t,i,lpan;
	freopen("B-large.in","r",stdin);
	freopen("Revenge of the Pancakes.out","w",stdout);
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>pan;
		lpan=strlen(pan);
		cout<<"Case #"<<i<<": "<<CantMan(pan,lpan)<<endl;
	}
	
	return 0;
}

