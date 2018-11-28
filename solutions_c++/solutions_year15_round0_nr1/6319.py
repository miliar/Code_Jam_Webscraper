#include <iostream>
using namespace std;


int main(){
	int n, caso=1;
	cin >> n;
	while(n--){
		int max, amigos=0, stand=0;
		string linha;
		cin >> max >> linha;
		for(int i=0;i<=max;i++){
			int ni = linha[i]-'0';
			int faltam = i - (stand + amigos);
			if(faltam > 0){
				amigos += faltam;
			}
			stand += ni;		
		}
		
		cout << "Case #"<< caso++ << ": "<<amigos<<endl;
	} 
	return 0;
}
