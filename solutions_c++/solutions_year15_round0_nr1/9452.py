#include <iostream>
using namespace std;

int main(){
	
	int n;
	cin>>n;
	for(int i=0;i<n;++i){
		int contador = 0;
		int peus = 0;		
		int m;
		cin >> m;
		for(int j=0;j<=m;++j){
			char aux;
			cin >> aux;
			int ent = aux - '0';
			if(peus<j){
				++contador;
				++peus;
			}
			peus = peus + ent;
		}
		cout<<"Case #"<<i+1<<": "<<contador<<endl;
	}
	
}
