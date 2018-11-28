#include<iostream>
using namespace std;

int main(){
	long long int n;
	int t=0,k=1;
	
	cin>>t;
	while(t--){
		string s;
		string r;
		cin>>s;	
		r=s[0];

		for(int i=1;i<s.length();i++){
			if(s[i]>=r[0]){
				r = s[i]+r;
			}
			else r=r+s[i];
		}
		cout<<"Case #"<<k++<<": "<<r<<endl;
	}	
	return 0;
}

