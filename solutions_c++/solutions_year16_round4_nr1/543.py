#include <bits/stdc++.h>
#include <fstream>
#include <stdio.h>
using namespace std;
vector<char> v;
void rec(int p,int r, int s){
	if((p+r+s)==1){
		if(p==1)v.push_back('P');
		if(r==1)v.push_back('R');
		if(s==1)v.push_back('S');
		return ;
	}
	if((p%2)==0){
		rec(p/2,r-(r/2),r/2);
		rec(p/2,r/2,r-(r/2));
	}
	if((r%2)==0){
		rec(p-(p/2),r/2,p/2);
		rec(p/2,r/2,p-(p/2));
	}
	if((s%2)==0){
		rec(p-(p/2),r/2,s/2);
		rec(p/2,r-(r/2),s/2);
	}
}

int main(){
	long long t,te,i,j,k,n,m,p,r,s;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>t;
	for(te=0;te<t;te++){
		fin>>n>>r>>p>>s;
		if((max(r,max(p,s))-min(r,min(p,s)))>1){
			string ans="IMPOSSIBLE";
			fout<<"Case #"<<(te+1)<<": "<<ans<<"\n";
			cout<<"Case #"<<(te+1)<<": "<<ans<<"\n";
			continue;
		}
		v.clear();
		rec(p,r,s);
		string ans="";
		for(i=0;i<v.size();i++){
			ans=ans+v[i];
		}
		fout<<"Case #"<<(te+1)<<": "<<ans<<"\n";
		cout<<"Case #"<<(te+1)<<": "<<ans<<"\n";

	}
	return 0;
}