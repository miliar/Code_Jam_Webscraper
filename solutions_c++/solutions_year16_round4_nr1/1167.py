#include <bits/stdc++.h>

using namespace std;
string build(string t,int n){
	if(n==0)return t;
	string res;
	t=build(t,n-1);
	for(int i=0;i<t.size();i++){
		if(t[i]=='R'){
			res=res+"RS";
		}else if(t[i]=='P'){
			res=res+"PR";
		}else{
			res=res+"PS";
		}
	}
	return res;
}
int count(string p,string qs){
	char q=qs[0];
	int res=0;
	for(int i=0;i<p.size();i++){
		res+=(p[i]==q);
	}
	return res;
}
string msort(string t){
	if(t.size()==1)return t;
	string res,l=t.substr(0,t.size()/2),r=t.substr(t.size()/2);
	l=msort(l);
	r=msort(r);
	if(l<r){
		return l+r;
	}else{
		return r+l;
	}
}
void process(string &t){
//	cout<<t<<endl;
	t=msort(t);
	cout<<t<<endl;
	return;
}
int main(){
	int tc,casen=1;
	cin>>tc;
	while(tc-->0){
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		string rs=build("R",n),ps=build("P",n),ss=build("S",n);
//		cout<<count(rs,"R")<<endl<<count(rs,"P")<<endl<<count(rs,"S")<<endl;
		cout<<"Case #"<<casen++<<": ";
		if(count(rs,"R")==r&&count(rs,"P")==p&&count(rs,"S")==s){
			process(rs);
		}else if(count(ps,"R")==r&&count(ps,"P")==p&&count(ps,"S")==s){
			process(ps);
		}else if(count(ss,"R")==r&&count(ss,"P")==p&&count(ss,"S")==s){
			process(ss);
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
