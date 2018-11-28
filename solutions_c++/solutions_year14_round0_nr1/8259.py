#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	
	int matriz[4][4];
	int vector[4];
	int cases, i, j, s, linea, contador_res, resultado;
	
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	
	
	cin >> cases;
	
	for(i=1; i<=cases; i++){
		contador_res=0;
		
		cin >> linea;
		for(j=0; j<4; j++){
			cin >> matriz[0][j] >> matriz[1][j] >> matriz[2][j] >> matriz[3][j];
		}
		
		vector[0]=matriz[0][linea-1];
		vector[1]=matriz[1][linea-1];
		vector[2]=matriz[2][linea-1];
		vector[3]=matriz[3][linea-1];
		
		
		cin >> linea;
		for(j=0; j<4; j++){
			cin >> matriz[0][j] >> matriz[1][j] >> matriz[2][j] >> matriz[3][j];
		}
		
		for(j=0; j<4; j++){
			for(s=0; s<4; s++){
				if(vector[j]==matriz[s][linea-1]){
					resultado=vector[j];
					contador_res++;
				}
			}
		}
		
		switch (contador_res) {
		case 0:
			cout <<"Case #"<<i<<": Volunteer cheated!"<<endl;
			break;
		case 1:
			cout <<"Case #"<<i<<": "<<resultado<<endl;
			break;
		default:
			cout <<"Case #"<<i<<": Bad magician!"<<endl;
			break;
		}
		
	}
	
	return 0;
}

