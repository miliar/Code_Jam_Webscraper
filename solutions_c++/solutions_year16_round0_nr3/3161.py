#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;
const long long MN=20;
long long mark[MN];
long long nm[MN];
long long divisor[MN];
long long output[100][50];
long long doutput[100][50];
long long N,J,con;
string rands(long long N){
	string x;
	for(long long i=1;i<N-1;i++){
		nm[i]=rand()%2;
	}
	nm[0]=1;
	nm[N-1]=1;
	return x;
}
long long giveval(long long b){
	long long num=0;
	for(long long i=0;i<N;i++){
		num*=b;
		if(nm[i]){
			num+=1;
		}
	}
	return num;
}

long long isprime(long long num){
	for(long long i=2;i<=sqrt(num)+1;i++){
		if(num%i==0){
			return i;
		}
	}
	return 0;
}
bool repeated(){
	for(long long i=0;i<con;i++){
		long long t=0;
		for(long long j=0;j<N;j++){
			if(output[i][j]!=nm[j]){
				t=1;
			}
		}
		if(t==0){
			return 0;
		}
	}
	return 1;
}
int main(){
	long long T;
	cin>>T;
	cin>>N>>J;
	con=0;
	while(con<J){
		cerr<<con<<endl;
		long long np=0;
		while(np==0){
			rands(N);
			if(!repeated()){
				continue;
			}
			np=1;
			for(long long i=2;i<=10;i++){
				long long num=giveval(i);
				cerr<<num<<endl;
				divisor[i]=isprime(num);
				if(divisor[i]==0){
					np=0;
					break;
				}
			}
		}

		for(long long i=0;i<N;i++){
			output[con][i]=nm[i];
			cerr<<nm[i]<<" ";
		}
		cerr<<endl;
		for(long long i=2;i<=10;i++){
			doutput[con][i]=divisor[i];
		}
		con++;
	}

		cout<<"Case #1:"<<endl;
	for(long long i=0;i<con;i++){
		for(long long j=0;j<N;j++){
			cout<<output[i][j];
		}
		for(long long j=2;j<=10;j++){
			cout<<" "<<doutput[i][j];
		}
		cout<<endl;
	}
}

			
		
