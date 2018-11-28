#include <bits/stdc++.h>

using namespace std;

int main(){
	int n=0,sm,r=0,c=0;
	string str;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>sm>>str;
		c=0,r=0;
		for(int j=0;r<sm&&j<=sm;j++){
			int si=str[j]-'0';
			if (si>0&&r<j){
				c+=j-r;
				r+=c;
			}
			r+=si;
		}
		cout<<"Case #"<<i+1<<": "<<c<<endl;
	}
	return 0;
}