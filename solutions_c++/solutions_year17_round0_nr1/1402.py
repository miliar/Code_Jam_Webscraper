#include<bits/stdc++.h>
using namespace std;
int main(){
	ifstream in("A-large.in.txt");
	ofstream out("output.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;++i){
		string s;
		in>>s;
		int d,ans=0;
		in>>d;
		for(int j=0;j!=s.size()-d+1;++j){
			if(s[j]=='-'){
				++ans;
				for(int k=j;k!=j+d;++k){
					if(s[k]=='-')
						s[k]='+';
					else
						s[k]='-';
				}
			}
		}
		string t(s.size(),'+');
		out<<"Case #"<<i<<": ";
		if(s==t)
			out<<ans;
		else
			out<<"IMPOSSIBLE";
		out<<endl;
	}
}