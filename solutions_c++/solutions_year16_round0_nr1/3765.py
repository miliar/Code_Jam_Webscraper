#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main(){
	ifstream fin("test.txt");
	ofstream fout("testrespuesta.txt");
	long int t;
	fin>>t;
	for(long int i=0; i<t; i++){
		long long int n;
		vector<bool> p(10,0);
		fin>>n;
		if(n==0){
			fout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n";	
		}else{
		long long int k=0;
		long long int w=0;
		bool comprobarmax=0;
		while(k<100000000){
			w+=n;
			k++;
			long long int y=w;
			while(y>0){
				int g=y%10;
				y=(y-g)/10;
				p[g]=1;
			}
			bool comprobar=1;
			for(int j=0;j<10;j++){
				if(!p[j]){
					comprobar=0;
					break;
				}
			}
			if(comprobar){
				comprobarmax=1;
				break;
			}
		}
		if(comprobarmax){
			fout<<"Case #"<<i+1<<": "<<w<<"\n";							
		}else{
			fout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n";				
		}
	}
}}
