#include <iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	cin.get();

	for(int i=1;i<=t;i++){
		string s;
		string lw;
		getline(cin, s);

		lw=s[0];
		for(int j=1;j<(int)s.size();j++){
			if(s[j]<lw[0]){
				lw=lw+s[j];
			}
			else{
				lw=s[j]+lw;
			}
		}
		
		cout<<"Case #"<<i<<": "<<lw.c_str()<<endl;
	}
}