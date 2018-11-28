#include <iostream>
#include <set>
using namespace std;
int main(){
	int T,N,M,i;
	set<int> S;
	cin>>T;
	for (int c = 1; c <= T; ++c){
		cin>>N;
		cout<<"Case #"<<c<<": ";	
		if(N==0)
			cout<<"INSOMNIA";
		else{
			S.clear();
			for (i = 1; S.size()<10; ++i){
				M=N*i;	
				while(M>0){
					S.insert(M%10);
					M/=10;
				}
			}
			cout<<(i-1)*N;
		}
		cout<<endl;
	}
	return 0;
}