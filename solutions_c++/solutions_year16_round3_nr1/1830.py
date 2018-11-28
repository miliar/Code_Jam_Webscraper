#include <iostream>
#include <string>
using namespace std;

int main(){
	int T;
	int N;
	int max1, max2, max3, imax1, imax2, imax3, suma;
	int P[30];
	char letras[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	string sol;
	string espacio = " ";
	cin>>T;
	for(int ii=0;ii<T;ii++){
		sol="";
		cin>>N;
		for(int jj=0;jj<N;jj++){
			cin>>P[jj];
		}
		cout<<"Case #"<<(ii+1)<<":";
		while(true){
			//encontrar maximo y agregar a la salida
			for(int i=0;i<N;i++){
				if(i==0){
					imax1=0;
					max1=P[0];
				}
				else{
					if(P[i]>max1){
						imax1=i;
						max1=P[i];
					}
				}
			}
			if(max1==0) break;
			sol = espacio+letras[imax1];
			//cout<<imax1<<" "<<max1<<" "<<sol;
			max1--;
			P[imax1]--;
			//encontrar segundo maximo y agregar a la salida si cabe
			for(int i=0;i<N;i++){
				if(i==0){
					imax2=0;
					max2=P[0];
				}
				else{
					if(P[i]>max2){
						imax2=i;
						max2=P[i];
					}
				}
			}
			P[imax2]--;
			for(int i=0;i<N;i++){
				if(i==0){
					imax3=0;
					max3=P[0];
					suma=P[0];
				}
				else{
					suma+=P[i];
					if(P[i]>max3){
						imax3=i;
						max3=P[i];
					}
				}
			}
			if((1.0*max3/2)>1.0*(suma-max3)) P[imax2]++;
			else{
				sol=sol+letras[imax2];
			}
			
			cout<<sol;
		}
		cout<<endl;
	}
}
