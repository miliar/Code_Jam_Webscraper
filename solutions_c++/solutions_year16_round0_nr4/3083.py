#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	int T,n;
	freopen("D-small.in","r",stdin);
	freopen("D-small.out","w",stdout);
	cin>>T;
	for(n=1;n<=T;n++)
	{
		int K,C,S,N,L;
		cin>>K>>C>>S;
		cout<<"Case #"<<n<<": ";
		if(K==1){cout<<1<<endl; continue;}
		if(C==1){
			N=K;
			if(S<N)cout<<"IMPOSSIBLE"<<endl;
			else {
			for(L=1;L<N;L++)cout<<L<<' ';
			cout<<K<<endl;
			}
		 continue;
		}
		N=(K>>1)+(K&1); 
		  L=2;
		  for(int i=1;i<N;i++){
		  	cout<<L<<" ";
		 	L+=2*K+2;		 	
		 }
		 if(K & 1)L-=K+1;
		 cout<<L<<endl;
				
	}
	return 0;
}
