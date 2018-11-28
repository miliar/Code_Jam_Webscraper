#include <iostream>
#include <cstdlib>
using namespace std;

short int tabla[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
int multiplicar(int a, int b){
	int aux;
	aux=tabla[abs(a)-1][abs(b)-1];
	if((a<0)^(b<0))
		return aux*(-1);
	else return aux;
}
int buscar1(string &cadena,int pos,int val){
	do{
		val=multiplicar(val,cadena[pos]);
		pos++;
	}
	while(val!=2&&pos<cadena.length());
	return pos;
}
int buscar2(string &cadena,int pos){
	int aux=1;
	do{
		aux=multiplicar(aux,cadena[pos]);
		pos++;
	}
	while(aux!=3&&pos<cadena.length());
	return pos;
}
bool buscar3(string &cadena,int pos){
	int aux=1;
	for(;pos<cadena.length();pos++) { 
		aux=multiplicar(aux,cadena[pos]);
	}
	return (aux==4);
}

int main() {
	int t;
	cin>>t;
	string aux,cadena;
	for(int i=1;i<=t;i++) { 
		int l,x;
		cin>>l>>x;
		cadena="";
		cin>>aux;
		for(int j=0;j<x;j++) { 
			cadena+=aux;
		}
		for(int j=0;j<cadena.length();j++) { 
			cadena[j]=cadena[j]-'i'+2;
		}
		int a=0,b,val=1;
		bool c=0;
		do{
			a=buscar1(cadena,a,val);
			if(a==cadena.length()) break;
			b=buscar2(cadena,a);
			if(b==cadena.length()) break;
			c=buscar3(cadena,b);
			val=2;
		}
		while(!c);
		cout<<"Case #"<<i<<": ";
		if (c)
			cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}

