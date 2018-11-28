#include<iostream>
#include<bits/stdc++.h>
using namespace std;


string revv(string s){
	string r;
	for(int i=0;i<s.size();i++) r+=s[s.size()-i-1];
	return r;
}

int main(){
	int t;cin>>t;
	for(int qq=1;qq<=t;qq++){
		int n;cin>>n;
		vector<int> v(n+1);
		v[1]=1;
		for(int i=2;i<=n;i++){
			string s=to_string(i);s=revv(s);int x=stoi(s);string ss=to_string(x);
			
			int pp=pow(10,ss.size());
			//cout<<v[x]<<endl;
			if(x<i && (x/pp==i/pp)){
				if(v[x]<v[i-1]) v[i]=v[x]+1;
				else v[i]=v[i-1]+1;
			}
			else v[i]=v[i-1]+1;
		}
		//for(int i=0;i<=n;i++) cout<<v[i]<<" ";cout<<endl;
		cout<<"Case #"<<qq<<": "<<v[n]<<endl;
	}
}
		
