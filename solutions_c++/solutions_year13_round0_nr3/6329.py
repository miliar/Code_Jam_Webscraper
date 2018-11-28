#include "competitive.h"
#include <cmath>

int digits(int x){
	int c=0;
	while (x>0){
		x/=10;c++;
	}
	
	return c;
}

int reverse(int x,int d){
	if(x<10) return x;
	return pow(10,d-1)*(x%10)+reverse(x/10,d-1);
	
}
	


bool ispalin(int x){
	
	if(x!=reverse(x,digits(x))) return false;
	
	return true;
}
	
	



int main(){
	int T;
	cin>>T;
	
	for(int i = 1;i<=T;i++){
		long long A,B;
		cin>>A>>B;
		int a=(int)sqrt(A);
		while(a*a<A) a++;
		int b=(int)sqrt(B);
		int c=0;
		for(int j =a;j<=b;j++)
			if (ispalin(j) && ispalin(j*j)) c++;
		
		cout<<"Case #"<<i<<": "<<c<<'\n';
		
		
	}

		
		
		
		
	
	return 0;
}
