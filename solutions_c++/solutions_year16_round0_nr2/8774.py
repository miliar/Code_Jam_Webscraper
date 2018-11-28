#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string flip(string S, int top){
	string ret="";
	for (int i=0;i<=top;i++){
		if (S[i]=='+') ret+="-";
		else ret+="+";
	}
	return ret;
}

int main(){
	int tc;
	cin>>tc;
	for (int t=1;t<=tc;t++){
		string S;
		int count=0;
		cin>>S;
		bool done=false;
		while (!done){
			//cout<<S<<endl;
			for (int i=S.size()-1;i>=0;i--){
				if (S[i]=='-') {S=flip(S,i); count++; break;}
				if (i==0) done=true;		
			}
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
}