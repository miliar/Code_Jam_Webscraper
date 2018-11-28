#include <bits/stdc++.h>

using namespace std;
int solve1(string t){
	int ch=0;
	for(int i=1;i<t.size();i++){
		ch+=(t[i]!=t[i-1]);
	}
	ch+=(t[t.size()-1]=='-');
	return ch;
}
int main(){
	int tc,i=0;
	cin>>tc;
	while(tc-->0){
		i++;
		string t;
		cin>>t;
		cout<<"Case #"<<i<<": "<<solve1(t)<<endl;
	}
	return 0;
}
