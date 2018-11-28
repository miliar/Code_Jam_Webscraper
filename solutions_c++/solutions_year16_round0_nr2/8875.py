#include<bits/stdc++.h>
using namespace std;
int main(){
//	freopen("B-small-attempt1.in","r",stdin);
//	freopen("B-small.attempt1.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int n;
	cin>>n;
	for(int t=1;t<=n;t++){
		string s;
		cin>>s;
		int count = 0;
		char tmp = s[0];
		for(char c : s){
			if(c!=tmp){
				count++;
				tmp = c;
			}
		}
		if(s[s.size()-1]=='-')	count++;
		cout<<"Case #"<<t<<": "<<count<<'\n';
	}
}
