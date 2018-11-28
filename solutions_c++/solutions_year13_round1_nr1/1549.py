#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

#define fori(i,n) for(int i = 0; i<n; i++)
#define pi 3.141592
typedef  unsigned long long int ull;

ull area(ull x,ull y){
	return pow(y,2)-pow(x,2);
}

int main(int argc, char *argv[]) {
	
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	ull n,r,t,result=0,aux;
	cin>>n;
	
	fori(i,n){
		cin>>r>>t;
		aux = area(r,r+1); 
		
		while(t>=aux){
			t -= aux;
			result++;
			r+=2;
			aux = area(r,r+1);
		}
		
		cout<<"Case #"<<i+1<<": "<<result<<endl;
		result = 0;
	}
	
	return 0;
}

