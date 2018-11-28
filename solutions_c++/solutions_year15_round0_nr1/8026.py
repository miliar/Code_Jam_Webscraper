#include <iostream>
using namespace std;

int main(){
	int ncasos,sMax, levantados,invitados;
	cin >> ncasos;
	for(int i=0; i<ncasos; i++){
		invitados=0;
		cin>>sMax;
		char datos[sMax+1];
		for(int j=0; j<=sMax; j++)
			cin>>datos[j];
		levantados = (int)(datos[0]-'0');
		for(int j=1; j<=sMax; j++){
			if(levantados+invitados<j){

				invitados++;
			}
			levantados+=(int)(datos[j]-'0');
		}
		cout<<"Case #"<<i+1<<": "<<invitados<<endl;
	}
}
