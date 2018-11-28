#include <iostream>
#include <stdio.h>
using namespace std;
int dgt [10];
int count=0;
int d;
void digits(int a){
	if(a==0) return;

	d=a%10;
	if(dgt[d]==0){
		count++;
	}
	dgt[d]++;
	a=a/10;
	digits(a);
}

int main() {
	int t,n;
	int aux;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}
		else{
			int k=1;
			while(count != 10){
				aux=k*n;
				digits(aux);
				k++;
			}
		cout<<"Case #"<<i+1<<": "<<aux<<endl;
		d=0;
		count=0;
		std::fill_n(dgt, 10, 0);
		}

	}
}