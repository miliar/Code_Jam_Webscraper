#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,te,n,i,j,k;
	string s;
	cin>>t;
	for(te=0;te<t;te++){
		cin>>k>>s;
		for(i=1,j=0,n=s[0]-'0';i<=k;i++){
			if(i>n){
				j+=(i-n);
				n=i;
			}
			n+=s[i]-'0';
		}
		cout<<"Case #"<<(1+te)<<": "<<j<<"\n";
	}
}