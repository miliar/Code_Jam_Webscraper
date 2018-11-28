#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,i,J;
	string s;
	cin>>t;
	for(J=1;J<=t;J++){
		cin>>s;
		string b;
		b.insert(b.begin(),s[0]);
		for(i=1;i<s.size();i++){
			if(s[i]>=b[0]){
			b.insert(b.begin(),s[i]);
			}
			else
			{
			b.insert(b.end(),s[i]);	
			}
		}
		cout<<"Case #"<<J<<": "<<b<<endl;
	}
}
