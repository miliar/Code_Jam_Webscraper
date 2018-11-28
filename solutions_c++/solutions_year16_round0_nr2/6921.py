#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int t;
string s;
int main(){
	ios::sync_with_stdio(0);
	cin.tie();cout.tie();
	cin>>t;
	for(int i=1;i<=t;i++){
		int ans=0;
		cin>>s;
		while(s.back()=='+')s.erase(s.length()-1);
		char now='+';
		for(int j=s.length()-1;j>=0;j--){
			if(s[j]!=now)ans++,now=s[j];
		}
		printf("Case #%d: %d\n",i,ans);
	}
}