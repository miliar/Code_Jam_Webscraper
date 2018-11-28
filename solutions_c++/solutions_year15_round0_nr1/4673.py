#include <bits/stdc++.h>
using namespace std;
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t; cin>>t;
	for(int i = 0; i < t; ++i){
		int n, sol = 0, c = 0; string s;
		cin>>n>>s; ++n;
		for(int j = 0; j < n; ++j){
			int x = s[j] - '0';
			if(j == 0) c += x;
			else if(j <= c) c += x;
			else { sol += j-c; c += (j-c) + x;}

		}
		cout<<"Case #"<<(i+1)<<": "<<sol<<"\n";

	}
	return 0;
}
