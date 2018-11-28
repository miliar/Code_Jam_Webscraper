#include<bits/stdc++.h>
using namespace std;
string flip(string s,int j){
	int i;
	for(i=0;i<=j;i++){
		if(s[i]=='+'){
			s[i]='-';
		}
		else{
			s[i]='+';
		}
	}
	return s;
}
int main()
{
	int t,i,j;
	long long count;
	string s;
	cin>>t;
	for(j=1;j<=t;j++){
		count=0;
		cin>>s;
		for(i=s.size()-1;i>=0;i--){
			if(s[i]=='-'){
				s=flip(s,i);
				count++;
			}
		}
		cout<<"Case #"<<j<<": "<<count<<endl;
	}
	return 0;
}
