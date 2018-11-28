#include <bits/stdc++.h>
#include <vector>
using namespace std;
vector<long long int> prim;
long long int esprimo(long long int num);
int main(){
	ifstream fin("test.txt");
	ofstream fout("testrespuesta.txt");
	vector<bool> to(100000,1);
	for(long long int i=2; i<100000; i++){
		if(to[i]){
			prim.push_back(i);
			long long int a=2*i;
			while(a<100000){
				to[a]=0;
				a+=i;
			}
		}
	}
	//cout<<"h";
	int n,t,max;
	fin>>t>>n>>max;
	vector<bool> numero(n,0);
	numero[0]=1;
	numero[n-1]=1;
	int total=0;
	fout<<"Case #1: "<<"\n";
	while(total<max){
		bool nosvale=1;
		queue<long long int> divisores;
		for(int j=2; j<=10; j++){
			long long int evalua=0;
			for(int w=0; w<n; w++){
				evalua+=numero[w]*pow(j,w);
			}
			long long int h=esprimo(evalua);
			if(h==-1){
				nosvale=0;
				break;
			}else{
			divisores.push(prim[h]);	
			}
		}
		if(nosvale){
			for(int w=n-1; w>=0; w--){
				fout<<numero[w];
			}
			while(divisores.size()){
				fout<<" "<<divisores.front();
				divisores.pop();
			}
			fout<<"\n";
			total++;	
			
		}
		int w;
		for(int w=1; w<n; w++){
			if(!numero[w]){
				numero[w]=1;
				break;
			}else{
				numero[w]=0;
			}
			
		}
		if(w==n) break;
	}
	
	
}

long long int esprimo(long long int num){
	long long int l=prim.size();
	float raiz=sqrt(num);
	bool primo=1;
	long long int y;
for(y=0; y<l && prim[y]<raiz ;y++){
if(num%prim[y]==0 && num!=prim[y]){
	primo=0;
	break;
}
}
if(primo){
	return -1;
}else{
	return y;
}
}
