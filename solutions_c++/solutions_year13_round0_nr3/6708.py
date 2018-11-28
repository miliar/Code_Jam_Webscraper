/*1	4 9 son palindromos*/
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

bool palindromo(float x){
	int tmp=x;
	int mod=0;
	int y=0;
	for(int i=0;tmp>0;i++){
		mod=tmp%10;
		y=(y*10)+mod;
		tmp/=10;
	}
	if(x==y)return true;
	return false;
}

int saf(int a,int b){
	int count=0;
	while(a<=b){
		float c=sqrt(a);
		if(palindromo(a) && palindromo(c))
			count++;
		a++;
	}
	return count;
}

int main() {
	int t;	//casos de prueba
	cin>>t;
	for(int i=0;i<t;i++){
			int a,b;
			cin>>a>>b;
			cout<<"Case #"<<i+1<<": "<<saf(a,b)<<endl;
	}
	return 0;
}

