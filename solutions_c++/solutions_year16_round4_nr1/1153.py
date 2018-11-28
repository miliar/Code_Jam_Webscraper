#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
#include<set>
#include<ctime>
using namespace std;
int n,R,P,S;
		
string f(string s, int niv){
	if(niv==0)return s;
	string dev="";
	for(int i=0;i<s.size();i++){
		char ch=s[i];
		if(ch=='R')
			dev+="RS";
		if(ch=='S')
			dev+="PS";
		if(ch=='P')
			dev+="PR";
	}
	
	return f(dev,niv-1);
}

bool funca(string s){
	int cr=0,cp=0,cs=0;
	for(int i=0;i<s.size();i++){
		if(s[i]=='R')cr++;
		if(s[i]=='P')cp++;
		if(s[i]=='S')cs++;
	}
	
	
	if(cr==R && cs==S && cp==P)return 1;
	return 0;
}

string g(string s){
	n=1<<n;
	
	for(int i=1; ;i++){
		if( (1<<i)>n )break;
		int t=1<<i;
		string dev="";
		for(int j=0;j<n;j+=t){
			int ini1= j;
			int fin1= j+t/2-1;
			int ini2= j+t/2;
			int fin2= j+t-1;
			string s1=s.substr(ini1,t/2);
			string s2=s.substr(ini2,t/2);
			if(s1<s2){
				dev+=s1;
				dev+=s2;	
			}else{
				dev+=s2;
				dev+=s1;
			}
		}
		s=dev;
	}
	return s;
}

int main(){
	
	int tc;
	cin>>tc;
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		cin>>n>>R>>P>>S;
		
		string p1=f("R",n);
		string p2=f("P",n);
		string p3=f("S",n);
		
		if(funca(p1) ){
			cout<<g(p1)<<endl;
			continue;
		}
		
		if(funca(p2) ){
			cout<<g(p2)<<endl;
			continue;
		}
		
		if(funca(p3) ){
			cout<<g(p3)<<endl;
			continue;
		}
		
		cout<<"IMPOSSIBLE"<<endl;
	}
	
    return 0;
}

