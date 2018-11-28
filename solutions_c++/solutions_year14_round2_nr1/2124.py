#include<iostream>
#include<string.h>
#include<string>
#include<stdio.h>
using namespace std;

string a,b;
void db(int x){
	a.erase(x,1);
}
void df(int x){
	a.insert(x,1,a[x-1]);
}
int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int nn,n,i,ans,r=1;
	cin>>nn;
	while(nn--){
		cin>>n;
		cin>>a>>b;
		if(a.length()>b.length()) swap(a,b);
		for(i=ans=0;i<a.length();i++){
			if(a[i]!=b[i]){
				if(i>0&&a[i-1]==b[i]){
					df(i);
					ans++;
				} 
				else {
					while(i>0&&i<a.length()-1&&a[i]==a[i-1]){
						db(i);
						ans++;
						if(a[i]==b[i]) break;
					}
					if(a[i]!=b[i]) break;
				}
			}
			if(a.length()>b.length()) swap(a,b);
		}
		if(i==a.length()){
			for(;i<b.length();i++){
				if(b[i]!=a[a.length()-1]) break;
				ans++;
			}
			if(i==b.length()) cout<<"Case #"<<r<<": "<<ans<<endl;
			else cout<<"Case #"<<r<<": Fegla Won"<<endl;
		}
		else cout<<"Case #"<<r<<": Fegla Won"<<endl;
		r++;
	}
	return 0;
}
/*
100
2
aaaaab
abbbb
*/