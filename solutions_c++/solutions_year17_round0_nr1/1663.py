#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t, k, n, ans;
	cin>>t;
	string s;
	for(int tc = 1; tc<=t; tc++){
		cin>>s;
		cin>>k;
		ans = 0;
		n = s.length();
		for(int i = 0; i<=n-k; i++){
			if(s[i]=='-'){
				for(int j = i; j<i+k; j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				ans++;
			}
		}
		int fl = 0;
		for(int i = 0; i<n; i++)
			if(s[i]=='-'){
				fl++;
				break;
			}
		cout<<"Case #"<<tc<<": ";
		if(fl)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}
