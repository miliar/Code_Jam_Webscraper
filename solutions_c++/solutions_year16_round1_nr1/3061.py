#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	int k=1;
	while(t--){
		string a;
		cin>>a;
		int f=5000,l=5000;
		char s[10000];
		for(int i=0;a[i];i++){
			if(f==l) s[l++]=a[i];
			else if(a[i]>=s[f]) s[--f]=a[i];
			else s[l++]=a[i];
		}
		cout<<"Case #"<<k<<": ";
		k++;
		for(int i=f;i<l;i++)
			cout<<s[i];
		cout<<'\n';
	}
}
			
