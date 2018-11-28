#include <bits/stdc++.h>
#include <vector>
#include <queue>
using namespace std;
int main(){
	ifstream fin("test.txt");
	ofstream fout("testrespuesta.txt");
	long int t;
	fin>>t;
	char b;
	fin.get(b);
	for(long int i=0; i<t; i++){
		vector<bool> lista;
		char a;
		while(1){
		fin.get(a);
		if(a=='+'){
			lista.push_back(1);
		}else{
			if(a=='-'){
				lista.push_back(0);
			}else{
				break;
			}
		}
		}
		long int lon=lista.size();
		bool u=0;
		long int total=0;
		bool primero=1;
		for(int j=0; j<lon;j++){
			if(lista[j] && u){
				if(primero){
				u=0;
				total+=1;					
				}else{
				u=0;
				total+=2;}
			}
			if(lista[j] && primero) primero=0;
			if(!lista[j]) u=1;
		}
		if(u && primero) total+=1;
		if(u && !primero) total+=2;
		fout<<"Case #"<<i+1<<": "<<total<<"\n";	
		
	}
}
