#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ofstream output;
	output.open("jj.txt");
	int t,k,c,s,ans;
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>k>>c>>s;
		if(k==1){
			 output<<"Case #"<<j<<": "<<"1"<<endl;
		}
		else if(c==1 && s==k){
			output<<"Case #"<<j<<": ";
			for(int i=1;i<=k;i++){
			   output<<i<<" ";
			}
			output<<" "<<endl;
		}
		else if(c==1 && s<k){
			 output<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		}
		else if(c>1 && s<k-1){
			 output<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		}
		else if(c>1 && s>k-1){
			output<<"Case #"<<j<<": ";
			for(int i=2;i<=k;i++){
			    output<<i<<" ";
			}
			output<<" "<<endl;

		}

	}

}