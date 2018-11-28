/*헤더 선언*/
#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

/* 상수 선언*/

/* 함수 선언*/

/* 전역변수 선언*/

int main()
{ 
	ifstream in; in.open("A-large.in"); //파일 입출력을 위한 초기화
	assert(in.is_open());
	ofstream out; out.open("A-large.out");
	int T; //number of test cases
	long long N;
	int digit[10]={0};
	int total_n=0;	//자릿수
	int count=0;
	in>>T;
	for(int i=1;i<=T;i++){
		for(int k=0;k<10;k++)
			digit[k]=0;
		in>>N;

	if(N==0)
			out<<"Case #"<<i<<": INSOMNIA"<<endl;
	else
		for(int y=1;;y++){
			count=0; total_n=0;
			for(int n=y*N;n>0;n=n/10)
				total_n++;

			for(int n=y*N;n>0;n=n/10)
				digit[n%10]=1;

			for(int k=0;k<10;k++){
				if(digit[k]==1)
					count++;
			}

			if(count==10){
				out<<"Case #"<<i<<": "<<y*N<<endl;
				break;
			}
		}
	}
		in.close(); out.close();
  return 0;
}