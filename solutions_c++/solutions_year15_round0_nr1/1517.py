#include<iostream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int t; cin>>t;
	for(unsigned int j=1; j<=t; j++){
		int maxS;
		cin>>maxS;
		char c[maxS+1];
		int nStanding = 0, nNeeded = 0;
		for (unsigned int i = 0; i <= maxS; i ++){
			cin>>c[i];
			nStanding += (int)(c[i]-'0');
			int k=i+1-nStanding;
			if(i<maxS && k>0){
				nNeeded += k;
				nStanding += k;
			}
		}
		cout<<"Case #"<<j<<": "<<nNeeded<<endl;
	}
	return 0;
}
