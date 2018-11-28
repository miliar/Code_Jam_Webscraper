#include<bits/stdc++.h>
using namespace std;

int main(){
int t,n,c=1;
freopen("A-small-attempt0.in","r", stdin);
freopen("output.in","w", stdout);
cin>>t;
while(c<=t){
	cin>>n;
	string s;
	cin>>s;
	int sum=0,res=0;
	for(int i=0;i<s.size();i++){
		sum+=s[i]-'0';
		if(s[i]=='0'&&sum<i+1) res++,sum++;
	}
	cout<<"Case #"<<c++<<": "<<res<<endl;
}
}
