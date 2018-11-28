#include <iostream>

using namespace std;

typedef long long int ll;

bool hash[10] = {false};

void updateHash(ll Num){
	while(Num){
		hash[Num%10] = true;
		Num /= 10;
	}
}

bool checkHash(){
	bool flag=true;
	int i;
	for(i=0;i<10;i++){		
		flag = flag & hash[i];
		//cout<<hash[i]<<" ";
	}
	return flag;
}

int main(){
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++){
		ll i,N;
		cin>>N;
		if(N==0){
			cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		for(i=0;i<10;i++) hash[i] = false;
		i=1;
		while(true){
		// a weak upper bound for no. of iterations of this loop is
		// (10^ceil(log10(N)+1)) / N which will never get more than 100
		// so a brute force soln suffices (ha-ha :D)
			//cout<<endl<<i<<endl;
			updateHash((i++) * N);
			if(checkHash())
				break;
		}		
		cout<<"Case #"<<t<<": "<<(i-1)*N<<endl;	
	}
	return 0;
}
