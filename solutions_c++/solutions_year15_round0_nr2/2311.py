#include<bits/stdc++.h>
using namespace std;

int main(){
	int N,NN;
	cin >> N;
	NN=N;
	while(N--){
		int n;
		cin >> n;
		int maxm=0;
		vector<int> v;
		v.resize(n);
		for(int i=0; i<n; i++){
			cin >> v[i];
			maxm=max(maxm,v[i]);
		}
		int ans=maxm;
		for(int k=1; k<=maxm;k++){
			int ret=0;
			for(int i=0; i<n; i++){
				if(v[i]>k){ 
					if(v[i]%k==0) ret+=v[i]/k -1;
					else ret+=(ceil(v[i]*1.0/k)-1);
				}
			}	
			ans=min(ans,ret+k);
		}
		printf("Case #%d: %d\n",NN-N,ans);
	}
}
