#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

#define fori(i,n) for(int i = 0; i<n; i++)
#define pi 3.141592
typedef  unsigned long long int ull;

int main(int argc, char *argv[]) {
	
	freopen("a4.in","r",stdin);
	freopen("a4.out","w",stdout);
	
	ull n,r,t,result=0,aux;
	cin>>n;
	
	fori(i,n){
		cin>>r>>t;
		aux = r+r+1; 
		
		while(t>=aux){
			t -= aux;
			result++;
			aux+=4;
		}

//		result = -1/2-sqrt(1+2*t);

//		while((t-=aux) > (aux+=4)){
//			
//		}
		
		cout<<"Case #"<<i+1<<": "<<result<<endl;
		result = 0;
	}
	
	return 0;
}

