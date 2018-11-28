#include <iostream>
#include <stdio.h>
using namespace std;

int contador(int n);
bool controlar(int a[]);

int main(int argc, char *argv[]) {
	int t, n,i;
	freopen("A-large.in","r",stdin);
	freopen("salidaLarge.out","w",stdout);
	cin >>t;
	for( i=1;i<=t;i++){
		cin >>n;
		if(n==0)cout<< "Case #"<<1 <<": INSOMNIA"<<endl;
		else{
			cout<<"Case #"<<i<<": "<<contador(n) <<endl;
		}

	}
	return 0;

}

int contador(int n){
	int i=1,num[10]={0,0,0,0,0,0,0,0,0,0},producto ;
	while(!controlar(num)){
		producto=n*i;
		while(true){
			if(num[producto%10]==0){
				num[producto%10]=1;
			}
			if (producto<10)
				break;
			producto=producto/10;
			}
		producto=n*i;
		i++;
		
		}
	return producto;
	}
	


bool controlar(int a[]){
	int i;
	for(i=0;i<10;i++)
		if(a[i]==0) return false;
	return true;
}

