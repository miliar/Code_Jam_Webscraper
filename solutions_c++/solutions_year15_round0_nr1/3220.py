#include<bits/stdc++.h>
using namespace std;
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("new.txt","w",stdout);
	int t;
	cin>>t;
	int f=0;
	while(t--){
		f++;
		int l; cin>>l;
		string a; cin>>a;
		long long int add=0, cur=0;
		for(int i=0; i<=l; i++){
			if(cur>=i){
				cur= cur+ a[i]-'0';
			}
			else{
				long long val=(long long)i-cur;
				add= (long long) add+val;
				cur= (long long) cur+val;
				cur= (long long) cur+a[i]-'0';
			}
		}
		cout<<"Case #"<<f<<": "<<add<<endl;
	}
}
