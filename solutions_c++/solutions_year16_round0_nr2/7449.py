#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,count,p,i,flag;
	string a;
	cin>>t;
	for(p=1;p<=t;p++){
		cin>>a;
		count;
		flag=0;
		count=0;
		for(i=1;i<a.size();i++){
			if(a[i-1]!=a[i]){
				count++;
			}
			
		}
		if(a[a.size()-1]=='-')
		cout<<"Case #"<<p<<": "<<count+1<<endl;
		else
		cout<<"Case #"<<p<<": "<<count<<endl;
	}
}
