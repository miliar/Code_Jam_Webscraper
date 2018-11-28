#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main(){
	ifstream fin("entrada.in");
	ofstream fout("salida.out");
	long long n;
	fin>>n;
	for(long long u=0;u<n;u++){
		fout<<"Case #"<<u+1<<": ";
		string p;
		fin>>p;
		long long a;
		fin>>a;
		long long t=0;
		for(long long i=0;i<p.size();i++){
			if(p[i]=='-' and i<=p.size()-a){
				t++;
				for(long long j=i;j<i+a;j++){
					if(p[j]=='+'){p[j]='-';}
					else{p[j]='+';}
				}
			}
		}
		long long h=0;
		for(long long i=0;i<p.size();i++){
			if(p[i]=='-'){h++;}
		}
		if(h!=0){fout<<"IMPOSSIBLE"<<endl;}
		else{fout<<t<<endl;}
	}
}
