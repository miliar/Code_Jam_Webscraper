#include <bits/stdc++.h>
using namespace std;
long T, ans, l;
string S;
int main(){
	cin>>T;
	for(int c=1; c<=T; c++){
		cin>>S;
		l = S.size();
		ans = 0;
		if(S[l-1]=='-') ans=1;
		for (int i = 1; i < l; ++i)
			if(S[i-1]!=S[i]) ans++;
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
}