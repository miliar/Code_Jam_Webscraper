#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	int T,i,j;
	freopen("Ds.in","r",stdin);
	freopen("Ds.out","w",stdout);
	cin>>T;
	for(i=1;i<=T;i++)
	{
		int K,C,S,N;
		cin>>K>>C>>S;
		//cout<<K<<" "<<C<<" "<<S<<endl;
		cout<<"Case #"<<i<<": ";
		if(K==1)cout<<1<<endl;
		else if(C==1){
			N=K;
			if(S<N)cout<<"IMPOSSIBLE"<<endl;
			else {cout<<1;
			for(j=2;j<=N;j++)cout<<' '<<j;
			cout<<endl;
			}
		} else {N=(K+1)>>1; 
		 int GN=0,LN=2;
		  while(--N){
		  	cout<<GN+LN<<" ";
		 	GN+=2*K; LN+=2;		 	
		 }
		 if(K & 1){GN-=2*K; LN--;
		 }
		 cout<<GN+LN<<endl;
		}		
	}
	return 0;
}
