#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin>>T;

	for(int K=1; K<=T; K++){
		string ans;
		string s;
		cin>>s;

		ans = s[0];
		for(int i=1; i<s.length(); i++){
			if(s[i] >= ans[0])
				ans = s[i] + ans;
			else
				ans = ans + s[i];
		}

		cout<<"Case #"<<K<<": "<<ans<<endl;
		// printf("Case #%d: %s\n", K, ans); 
	}

	return 0;
}