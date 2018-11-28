#include <iostream>
#include <vector>
using namespace std;
long long primo(long long n){
	for(long long i=2;i*i<=n;i++) { 
		if(n%i==0)
			return i;
	}
	return 0;
}
long long base(int a, int i){
	int mask=1;
	long long res=0;
	long long exponente=1;
	while(mask<=a){
		if(a&mask)
			res+=exponente;
		exponente*=i;
		mask<<=1;
	}
	return res;
}
int main(int argc, char *argv[]) {
	int t;
	cin>>t;
	cout<<"Case #1:"<<endl;
	int n,j;
	cin>>n>>j;
	int a=0;
	a|=1<<(n-1);
	a|=1;
	for(;a<1<<n && j;a+=2){
		vector<long long> res(9,0LL);
		bool sol=1;
		for(int i=2;i<=10;i++){
			res[i-2]=primo(base(a,i));
			if(res[i-2]==0)
				sol=0;
		}
		if(sol){
			j--;
			cout<<base(a,10)<<" ";
			for(int i=0;i<9;i++) { 
				cout<<" ";
				cout<<res[i];
			}
			cout<<endl;
		}
	}
	
	return 0;
}

