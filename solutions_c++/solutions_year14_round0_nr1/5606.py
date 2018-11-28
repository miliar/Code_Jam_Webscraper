#include <iostream>
#include <cctype>
#include <algorithm>
#include <vector>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
	freopen("A-small-attempt1.in","r", stdin);//Entradas desde archivo.
	freopen("A-small-attempt1.out", "w", stdout);//Salidas a archivo.
	int rep, f1, f2, aux3;
	vector<int> f11, f12, f13, f14, f21, f22, f23, f24, aux1, aux2, interseccion;
	
	cin>>rep;
	rep++;
	for(int j=1;j<rep;j++){
		cin>>f1;
		for(int i=0; i<4;i++){
			cin>>aux3;
			f11.push_back(aux3);
		}
		for(int i=0; i<4;i++){
			cin>>aux3;
			f12.push_back(aux3);
		}
		for(int i=0; i<4;i++){
			cin>>aux3;
			f13.push_back(aux3);
		}
		for(int i=0; i<4;i++){
			cin>>aux3;
			f14.push_back(aux3);
		}
		cin>>f2;
		for(int i=0; i<4;i++){
			cin>>aux3;
			f21.push_back(aux3);
		}
		for(int i=0; i<4;i++){
			cin>>aux3;
			f22.push_back(aux3);
		}
		for(int i=0; i<4;i++){
			cin>>aux3;
			f23.push_back(aux3);
		}
		for(int i=0; i<4;i++){
			cin>>aux3;
			f24.push_back(aux3);
		}

		switch(f1){
		case 1: aux1=f11;break;
		case 2: aux1=f12;break;
		case 3: aux1=f13;break;
		case 4: aux1=f14;break;
		}
		switch(f2){
		case 1: aux2=f21;break;
		case 2: aux2=f22;break;
		case 3: aux2=f23;break;
		case 4: aux2=f24;break;
		}
		sort(aux1.begin(), aux1.end());
		sort(aux2.begin(), aux2.end());
		set_intersection(aux1.begin(),aux1.end(),aux2.begin(),aux2.end(),back_inserter(interseccion));
		if(interseccion.size()==0){
			cout<<"Case #"<<j<<": "<<"Volunteer cheated!"<<endl;
		}
		else if(interseccion.size()==1){
			cout<<"Case #"<<j<<": "<<interseccion[0]<<endl;
		}
		else{
			cout<<"Case #"<<j<<": "<<"Bad magician!"<<endl;
		}
		f11.clear();
		f12.clear();
		f13.clear();
		f14.clear();
		f21.clear();
		f22.clear();
		f23.clear();
		f24.clear();
		aux1.clear();
		aux2.clear();
		interseccion.clear();
	}
	return 0;
}
