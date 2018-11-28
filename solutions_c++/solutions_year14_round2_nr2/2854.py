#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std ;


int main(int argc,char* argv[]){
	ifstream is ;
	is.open("B-small-attempt0.in", std::ifstream::in);
	ofstream os ;
	os.open("B.out", std::ifstream::out);
	int num ;
	is >>num ;
	int A,B,K,count=0;
	for(int i=0;i<num;i++){
		is >> A;
		is >> B;
		is >> K;
		for(int i=0;i<A;i++){
			for(int j=0;j<B;j++){
				if((i&j)<K)
					count++ ;
			}
		}
		os<<"case #"<<i+1<<": "<<count<<endl;
		count = 0 ;
	}
}

