#include <bits/stdc++.h>

using namespace std;

#define crivoSize 11111111
bool p[crivoSize];

long long teste(long long n,long long base){
	long long ans=0;
	long long aux=1;
	if(base!=10){
		while(n!=0){
			ans+=aux*(n%10);
			n/=10;
			aux*=base;
		}
	}
	else
		ans=n;
	if(ans<crivoSize){
		if(p[ans])
			return 0;
		else{
			int i=2;
			while(ans%i!=0)
				i++;
			return i;
		}
	}
	for(int i=2;i<=sqrt(ans);i++)
		if(ans%i==0)
			return i;
	return 0;
}

void crivo(){
	int aux;
	p[0]=false;
	p[1]=false;
	for(int i=2;i<=crivoSize/2;i++)
		if(p[i]){
			for(int j=2*i;j<crivoSize;j+=i)
				p[j]=false;
		}
	return;
}

int main(){
	int t;
	int n;
	int j;
	unsigned long long aux=1000000000000001;
	memset(p,1,sizeof(p));
	vector<int> div;
	crivo();
	int cont=0;
	int cont2;
	bool bizu;
	//cin>>t;
	//cin>>n;
	//cin>>j;
	cout<<"Case #1:\n";
	while(cont<50){
		bizu=true;
		div.clear();
		for(int i=2;i<=10;i++){
			div.push_back(teste(aux,i));
			if(!div.back()){
				bizu=false;
				break;
			}
		}
		//cout<<aux;
		if(bizu){
			cont++;
			cout<<aux;
			for(int i=0;i<div.size();i++)
				cout<<" "<<div[i];
			cout<<"\n";
		}
		//cout<<"\n";
		cont2=0;
		while(aux%10==1){
			cont2++;
			aux/=10;
		}
		aux++;
		while(cont2--)
			aux*=10;
		aux++;
	}
	return 0;
}