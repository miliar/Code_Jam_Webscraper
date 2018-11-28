#include <iostream>
#include <vector>
using namespace std;

main(){
	long long T;
	cin>>T;
	for(long long t=0;t<T;t++){
		long long N;
		cin>>N;
		if(N==0) cout<<"Case #"<<t+1<<": "<<"INSOMNIA\n";
		else{
			vector<long long> hash(10,0);
			long long cnt=0;
			for(long long x=1;cnt<10;x++){
				long long prod = x*N;
				while(prod>0){
					long long y=prod%10;
					if(hash[y]==0){
						cnt++;
						hash[y]=1;
					}
					prod=prod/10;
				}
				if(cnt==10) cout<<"Case #"<<t+1<<": "<<x*N<<"\n";
			}
		}
	}
}