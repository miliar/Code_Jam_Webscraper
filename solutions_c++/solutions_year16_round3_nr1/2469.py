//A
#include <bits/stdc++.h>
using namespace std;
int vet[30];

int maior(int t){
	int x = 0;
	for (int i = 1; i < t; i++)
	{
		if(vet[x]<vet[i])x = i;
	}
	return x;
}

int maior2(int t){
	int ex = maior(t);
	int x = 0;
	for (int i = 1; i < t; i++)
	{
		if(!(ex==i))
			if(ex==x ||vet[x]<vet[i])x = i;
	}
	return x;
}

bool evacuado(int t){
	for (int i = 0; i < t; i++)
	{
		if(vet[i])return false;
	}
	return true;
}

int soma(int t){
	int s=0;
	for (int i = 0; i < t; i++)
	{
		s+=vet[i];
	}
	return s;
}

int main(){
	int t,t1;
	cin>>t;
	t1 = t;
	while(t--){
		cout<<"Case #"<<t1-t<<":";
		int n;
		cin>>n;
		
		memset(vet,0,sizeof(vet));
		for (int i = 0; i < n; i++)
		{
			cin>>vet[i];
		}
		while(!evacuado(n)){
			int ind=maior(n);
			int m = vet[ind];
			int ind2 = maior2(n);
			int m2 = vet[ind2];
			int s=soma(n);
			if(m2 == 1 && m==1 && s==2){//Final
				cout<<" "<<(char)('A'+ind)<<(char)('A'+ind2);
				vet[ind]-=1;
				vet[ind2]-=1;
			}else if(m==1&&m2==1 && s>2){
				cout<<" "<<(char)('A'+ind);
				vet[ind]-=1;
			}else if(s-1<=m2*2){
				cout<<" "<<(char)('A'+ind)<<(char)('A'+ind2);
				vet[ind]-=1;
				vet[ind2]-=1;
			}else if(s-2<=m2*2){
				cout<<" "<<(char)('A'+ind);
				vet[ind]-=1;
			}else{
				cout<<" "<<(char)('A'+ind)<<(char)('A'+ind);
				vet[ind]-=2;
			}
			
		}
		cout<<endl;
	}
	
	return 0;
}
