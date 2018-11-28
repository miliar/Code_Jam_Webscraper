#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(){
	ifstream archivoSaldos("A-large-attempt0.in");
	ofstream archivo("largeresult.txt");
	int t=0, n, aux=1, auxn, result, i, auxsize;
	char linea[10];
	archivoSaldos.getline(linea, 10);
	auxsize = 0;
	while(linea[auxsize]>0){
		t*=10;
		t+=(linea[auxsize] - '0');
		auxsize++;
	}
	bool digit[11];
	for(; aux<=t; aux++){
		n=0;
		archivoSaldos.getline(linea, 10);
		auxsize = 0;
		while(linea[auxsize]>0){
			n*=10;
			n+=(linea[auxsize] - '0');
			auxsize++;
		}
		archivo<<"Case #"<<aux<<": ";
		if(n==0){
			archivo<<"INSOMNIA";
		}
		else{
			digit[0]=digit[1]=digit[2]=digit[3]=digit[4]=digit[5]=digit[6]=digit[7]=digit[8]=digit[9]=false;
			digit[10] = true;
			i=0;
			while(digit[10]){
				i++;
				auxn = i*n;
				result = (int) log10(auxn);
				result++;
				while(result>0){
					digit[auxn%10] = true;
					auxn=auxn/10;
					result--;
				}
				if(digit[0]&&digit[1]&&digit[2]&&digit[3]&&digit[4]&&digit[5]&&digit[6]&&digit[7]&&digit[8]&&digit[9])	digit[10]=false;
			}
			archivo<<i*n;
		}
		archivo<<endl;
	}
	archivoSaldos.close();
	archivo.close();
	return 0;
}
