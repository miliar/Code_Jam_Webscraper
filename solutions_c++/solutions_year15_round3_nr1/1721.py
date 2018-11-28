#include<bits/stdc++.h>

using namespace std;


int main(){
	int t;
	cin>>t;

	for(int te=0;te<t;te++){
		int r,c,w;
		cin>>r>>c>>w;

		int res;
		if(w==1){
			res = c*r;
		}
		else{
			res = (c-1)/w*r + w;
		}
		cout<<"Case #"<<(te+1)<<": "<<res<<endl;
	}
}