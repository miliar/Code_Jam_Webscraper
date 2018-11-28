#include<iostream>
#include<cstdio>
using namespace std;
bool A[10];

void digitcompare(unsigned long long a){
	int x;
	x=a%10;
	while(a!=0){
		A[x]=1;
		a/=10;
		x=a%10;
	}
}
bool confirmans(){
	bool flag=true;
	for(int i=0;i<10;i++){
		if(A[i]==false){
			flag=false;
		}
	}
	return flag;
}
void arrclr(){
	for(int i=0;i<10;i++){
		A[i]=false;
	}
}

int main(){
	unsigned long long T,N;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>N;
		int j;
		arrclr();
		for(j=1;j<=100;j++){
			int k=N*j;
			digitcompare(k);
			bool s=confirmans();
			if(s==true){
				break;
			}
		}
		if(j==101)
			printf("Case #%d: INSOMNIA \n",i+1);
		//i+1 for 0 start
		else
			printf("Case #%d: %llu \n",i+1,j*N);
	}
	return 0;
}