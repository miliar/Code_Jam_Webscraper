#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
/*

jwkim0000@gmail.com
CodeJam nickname : JackRabbit

*/
using namespace std;

int getResult(int min, int max);
inline int isSq(int n);
inline int isPa(int n);
int main(){
	int howMany=0;
	string str;
	int min, max;

	ifstream fin("C-small-attempt2.in");
	ofstream out("C-small-attempt2.out");

	fin>>howMany;
	for(int k=0; k<howMany;k++){
		fin>>min>>max;
		out<<"Case #"<<(k+1)<<": "<<getResult(min,max)<<endl;
		//cout<<"test : "<<min<<" "<<max<<endl;
		//cout<<"test :"<<getResult(min,max)<<" "<<endl;	//	debug code	
	}

	return 0;
}

int getResult(int min,int max){
	int count=0;
	for(int i=min;i<=max;i++){
		if(isSq(i) && isPa(i)){
			count++;
		}
	}
	return count;
}
inline int isSq(int n){
	int k;
	for(k=1;k<=n;k++){
		if((k*k)==n&&isPa(k))
			return 1;
	}
	return 0;
}
inline int isPa(int n){
	char num[15];
	itoa(n,num,10);
	int len = strlen(num);
	for(int i=0;i<=(len/2);i++){
		if(num[i]!=num[len-i-1])
			return 0;
	}
	return 1;
}