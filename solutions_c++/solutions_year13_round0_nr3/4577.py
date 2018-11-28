#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

bool palindromo(int a)
{
	char s[4];
	int aux=a;
	int alg=0;
	int dez=1;
	while(aux!=0)
	{
		s[alg]=aux%10;
		aux/=10;
		alg++;
	}
	for(int i=alg-1;i>=0;i--)
	{
		aux+=s[i]*dez;
		dez*=10;
	}
	if(aux==a)
		return true;
	return false;
}

int main()
{
	int t;
	int inicio,fim,inicio2;
	int cont=1;
	int quant;
	float raiz;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>inicio;
		cin>>fim;
		quant=0;
		raiz=inicio;
		raiz=sqrt(raiz);
		inicio2=raiz;
		for(int j=inicio2;j*j<=fim;j++)
			if(palindromo(j) && palindromo(j*j) && j*j>=inicio)
				quant++;
		cout<<"Case #"<<cont<<": "<<quant<<"\n";
		cont++;
	}
}