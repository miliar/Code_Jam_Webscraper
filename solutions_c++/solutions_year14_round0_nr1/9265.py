#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	
	int t;
	
	cin>>t;
	int* matriz = new int[17];
	
	int caso = 1;
	while(t--){
		for(int i = 0; i < 17; i++)matriz[i] = 0;
		int r,s,k;
		cin>>r;
		for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
						cin>>k;
						if(i == r-1){
							matriz[k]++;
						}
					}
		}
		cin>>s;
		for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
						cin>>k;
						if(i == s-1){
							matriz[k]++;
						}
					}
		}
		int suma = 0;
		int posicion;
		for(int i = 0; i < 17; i++){
			if(matriz[i] > 1){suma++;posicion = i;}
		}		
		if(suma == 0) printf("Case #%d: %s\n",caso++,"Volunteer cheated!");
		else if(suma > 1)printf("Case #%d: %s\n",caso++,"Bad magician!");
		else{
			printf("Case #%d: %d\n",caso++,posicion);
		}
	}	


return 0;
}
