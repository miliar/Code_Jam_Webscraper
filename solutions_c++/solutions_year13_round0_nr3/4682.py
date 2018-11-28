#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

typedef unsigned long long int type;
bool esPali(type);

int main()
{
	type czo,final,cuenta,raiz1,raiz2,T,caso=1,cuadrado;
	ifstream fin("large1.in");
	ofstream fout("salidaLarga1.txt");
	fin>>T;
	while(T--){
		fin>>czo>>final;
		raiz1=ceil(sqrt(czo));
		raiz2=sqrt(final);
		cuenta=0;
		for(type i=raiz1;i<=raiz2;i++){
			cuadrado=i*i;
			if(esPali(i)){
				if(esPali(cuadrado)){
					cuenta++;
					//cout<<i<<" "<<cuadrado<<endl;	
				}
			}
		}
		fout<<"Case #"<<caso<<": "<<cuenta<<endl;
		caso++;
	}




	return 0;
}

bool esPali(type n)
{
	bool ans=true;
	type original=n,reverse=0,digit;
	while(n>0){
		digit=n%10;
		reverse=reverse*10+digit;		
		n/=10;
	}
	ans=(original==reverse)?true:false;
	return ans;
}
