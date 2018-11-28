#include <bits/stdc++.h>
using namespace std;
int main(){
	int test,a;
	string s;
	scanf("%d",&test);
	for (int j = 1; j <= test; j++) {
		cin>>a>>s;
		int count=0,ans=0;
		for (int i = 0; i < s.length(); i++) {
			if(count<i) ans+=i-count,count+=i-count;
			count+=s[i]-'0';
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
}