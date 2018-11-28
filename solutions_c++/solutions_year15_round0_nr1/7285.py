#include <iostream>
#include <map>

#include <algorithm>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[]) {
	long t,  contador=0, agregados=0;
	int smax;
	
	string entrada;
	
	cin >> t;
	
	for (int i=1;i<=t;i++){
		map<int,int> restantes;
		cin >> smax;
		cin >> entrada;
		contador = entrada.at(0) - '0';
		
		for(long j = 1 ; j<=smax;j++){
			if(j <= contador)
				contador += entrada[j] - '0';
			else 
				restantes[j]=entrada[j] - '0';
		}
		
		if(restantes.empty())
			cout << "Case #"<<i<<": "<<0<<endl;
		else{
			contador++;
			agregados=1;
			map<int,int>::const_iterator it = restantes.begin();
			while(it!=restantes.end()){
				if(it->first <= contador){
					contador += restantes[it->first];
					it++;
				}
				else{
					agregados++;
					contador++;
				}
			}
			cout << "Case #" << i << ": " << agregados << endl;
			}

	}
	return 0;
}

