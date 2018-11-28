#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {

	int T,i,ctr,flag,k=1;

	unsigned long int a=0,N,num;



	cin>>T;
	while(T){
		i=1;
		a=0;
		cin>>N;

		flag=0;

		while(flag==0){
			num=i*N;
			if(num>=1000000||num==0){
					flag=1;
					cout<<"Case #"<<k++<<": INSOMNIA"<<endl;
					break;
				}
			while(num){
				a = a|(1<<(num%10));
				num=num/10;
				if(a>=1023){
					flag=1;
					cout<<"Case #"<<k++<<": "<<i*N<<endl;
					break;
				}
			}
			++i;
		}
        --T;



	}
	return 0;
}
