#include<iostream>
#include<fstream>
using namespace std;

ofstream fout("lot.out");

int T;
int A,B,K;

int main(){
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>A>>B>>K;
		int count=0;
		for(int i=0;i<A;i++){
			for(int j=0;j<B;j++){
				//cout<<i<<" "<<j<<" "<<(i & j)<<endl;
				if((i & j) < K)count++;
			}
		}
		fout<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}