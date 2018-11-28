#include <iostream>
#include <string>

using namespace std;

int main(){
	int t,out;
	cin>>t;
	string seq,curr;
	for(int i=0;i<t;i++){
		out=0;
		cin>>seq;
		curr = seq[0];
		if(curr=="-"){
			out++;
		}
		for(int j=1;j<(int)seq.length();j++){
			if(seq[j]!=seq[j-1]&&seq[j]=='-'){
				out+=2;
			}
		}
		cout<<"Case #"<<i+1<<": "<<out<<"\n";
	}
	return 0;
}