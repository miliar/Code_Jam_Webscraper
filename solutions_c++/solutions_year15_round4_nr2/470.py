#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int N,M,K,Q,T;
double V,X;
double rate[103];
double degree[103];

int main(){
	cin>>T;
	for(int cs=1; cs<=T;++cs){
		cin>>N>>V>>X;
		for(int i=0;i<N;++i){
			cin>>rate[i]>>degree[i];
		}
		if(N==1){
			if(degree[0]==X)
				printf("Case #%d: %.7lf\n", cs, V/rate[0]);
				//cout<<"Case #"<<cs<<": "<<(V/rate[0])<<endl;
			else
				printf("Case #%d: IMPOSSIBLE\n", cs, V/rate[0]);
				//cout<<"Case #"<<cs<<": "<<"IMPOSSIBLE"<<endl;
		}else{
			if(degree[1]==degree[0]){
				if(degree[0]==X)
					printf("Case #%d: %.7lf\n", cs, V/(rate[1]+rate[0]));
					//cout<<"Case #"<<cs<<": "<<(V/(rate[0]+rate[1]))<<endl;
				else
					cout<<"Case #"<<cs<<": "<<"IMPOSSIBLE"<<endl;
				continue;
			}
			if(degree[1]==X){
					printf("Case #%d: %.7lf\n", cs, V/(rate[1]));
				//cout<<"Case #"<<cs<<": "<<(V/(rate[1]))<<endl;
				continue;
			}
			if(degree[0]==X){
					printf("Case #%d: %.7lf\n", cs, V/(rate[0]));
				//cout<<"Case #"<<cs<<": "<<(V/(rate[0]))<<endl;
				continue;
			}
			if( (degree[0]>X && degree[1]<X) || (degree[0]<X && degree[1] >X)){
				double V1= (X*V-V*degree[0])/(degree[1]-degree[0]);
				double V0= (X*V-V*degree[1])/(degree[0]-degree[1]);
					printf("Case #%d: %.7lf\n", cs, max(V0/rate[0], V1/rate[1]));//V/(rate[1]+rate[0]));
				//cout<<"Case #"<<cs<<": "<<max(V0/rate[0], V1/rate[1])<<endl;
				continue;
			}
			cout<<"Case #"<<cs<<": "<<"IMPOSSIBLE"<<endl;

		}

	}

	return 0;
}


