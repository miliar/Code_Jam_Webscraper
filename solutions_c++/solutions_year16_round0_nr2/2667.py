#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	ll t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		string s; cin>>s;
		ll sol = 0; int st = -1, en = -1, n = s.length();
		for(int j = 0; j < n; ++j){
			if(s[j] == '-'){
				if(st == -1) st = j;
			}
			else {
				if(st != -1) {
					en = j - 1;
					//st = -1;
				}
			}
			//cout<<j<<" "<<s[j]<<" "<<st<<" "<<en<<endl;
			if(st != -1 && en != -1){
				if(st == 0) sol += 1;
				else sol += 2;
				st = -1; en = -1;
			}
			else if(st == 0 && j == n-1) sol += 1;
			else if(st != -1 && j == n-1) sol += 2;
		}
		cout<<"Case #"<<(i+1)<<": "<<sol<<"\n"; 
	}
	return 0;
}
