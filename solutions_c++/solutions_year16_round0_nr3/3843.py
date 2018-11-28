/*헤더 선언*/
#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;
#define SIZE 16
long long power(long long a,int n);
long long divisor(long long sum);

int main()
{ 
	ifstream in; in.open("C-small-attempt0.in");
//	assert(in.is_open());
	ofstream out; out.open("C-small-attempt0.out");
	int T; //number of test cases
	int N, J;
	int count=0;
	int num_J=0;
	int P[SIZE]={0};
	int Reverse[SIZE]={0};
	long long Divisor[11]={0};

//	in>>T;
	T=1;

	for(int i=1;i<=T;i++){
//		in>>N>>J;
		N=16;
		J=50;

		out<<"Case #"<<i<<":"<<endl;

		for(long long j=1+power(2,N-1);j<power(2,N);j=j+2) {		//j를 number라 보면됌
			long long number=j;
			long long sum=0;
			count=0;
			//2진수 구하기 배열에 집어넣기 : 수 만들기
			for(int k=0;number>0;k++){
				Reverse[k]=number%2;
				number=number/2;
			}
			for(int k=0;k<N;k++){
				P[k]=Reverse[N-k-1];
			}

			for(int base=2;base<=10;base++){
				sum=0;
				for(int n=0;n<N;n++)
					sum+=Reverse[n]*power(base,n);

				if(divisor(sum)>0)
					count++;
				Divisor[base]=divisor(sum);
				
			}
			if(count==9){
				num_J++;
				for(int k=0;k<N;k++)
					out<<P[k];
				out<<" ";
				for(int base=2;base<=10;base++)
					out<<Divisor[base]<<" ";
				out<<endl;
			}
			if(num_J==J)
				break;
		
		}

	}
		in.close(); out.close();
  return 0;
}

long long power(long long a,int n){
  if(n==0)
	  return 1;
  else if(n==1) 
	 return a;
  if (n%2==0)
	  return power(a*a, n/2);
  return a*power(a*a,(n-1)/2);
}

long long divisor(long long sum){
	int count=0;
	for(long long i=1;i<power(2,15);i++){
		if(sum%i==0)
			count++;
		if(count>=2)
			return i;
	}
	return -1;
}