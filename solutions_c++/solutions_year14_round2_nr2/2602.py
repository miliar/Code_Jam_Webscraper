#include <iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		long long A,B,K;
		cin>>A;
		cin>>B;
		cin>>K;
		long long temp;
		long long count=0;
		for(long long j=0;j<A;j++){
			for(long long k=0;k<B;k++){
				temp = j&k;
				if(temp<K){
					count+=1;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;		
	}
}
