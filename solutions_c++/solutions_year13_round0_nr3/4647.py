#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<math.h>
#define MAXN 100000000
using namespace std;
long long squares[MAXN][2];

void initsquares(unsigned b){
  unsigned i;
  for(i=0;i<b;i++){
	squares[i][0]=i+1;
	squares[i][1]=(i+1)*(i+1);
	}
}

long long fastPow(long long x,int i){
	if(i==0) return 1;
	if(i==1) return x;
	else if(i%2) return x*fastPow(x,i-1);
			else return fastPow(x*x,i/2);
}

unsigned retrIdig(long long num,int n){
	long long temp = (num/fastPow(10,n))*10;
	return num/fastPow(10,n-1)-temp;
}
	
bool testPal(long long num){
	int i=1,j;
	if(!num/10) return true;
	while(1) {
		long long c=fastPow(10,i);
		if(num/c)
		i++;
		else break;
	}
	for(j=1;j<=i/2;j++){
		if(retrIdig(num,i-j+1)!=retrIdig(num,j)) return false;
	}
	return true;
}

unsigned palInRange(long long A, long long B){
	unsigned i,temp;
	unsigned counter=0;
	unsigned b=(unsigned)sqrt(B);
	initsquares(b);
	for(i=0;i<b;i++)
	{
		if(squares[i][1]==A) temp=i;
		else
		if(squares[i][1]<A&&squares[i+1][1]>=A) temp=i+1;
	}
	for(i=temp;i<b;i++)
	{
		if(testPal(squares[i][0])&&testPal(squares[i][1])) {//cout<<squares[i][0]<<" "<<squares[i][1]<<"\n";
		 counter++;}
	}
	return counter;
}

int main(void){
	int i,T;
	unsigned A,B;
	cin>>T;
	int value[T];
	for(i=0;i<T;i++){
			cin>>A>>B;
			value[i]=palInRange(A,B);
		}
	for(i=0;i<T;i++){
		printf("Case #%d: %d\n",i+1,value[i]);
	}
return 0;
}

