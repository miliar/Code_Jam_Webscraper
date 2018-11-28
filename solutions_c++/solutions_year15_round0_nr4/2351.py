#include <bits/stdc++.h>
using namespace std;
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t; cin>>t;
	for(int i = 0; i < t; ++i){
		int x, r, c;
		cin>>x>>r>>c;
		int l = r*c;
		if(x == 1) {
			cout<<"Case #"<<(i+1)<<": GABRIEL"<<"\n"; 
		}
		else if(x == 2){
			if(l % 2) cout<<"Case #"<<(i+1)<<": RICHARD"<<"\n"; 
			else cout<<"Case #"<<(i+1)<<": GABRIEL"<<"\n"; 
		}
		else if(x == 3){
			if(l == 6 || l == 9 || l == 12) cout<<"Case #"<<(i+1)<<": GABRIEL"<<"\n"; 
			else cout<<"Case #"<<(i+1)<<": RICHARD"<<"\n"; 
		}
		else if(x == 4){
			if(l == 12 || l == 16) cout<<"Case #"<<(i+1)<<": GABRIEL"<<"\n"; 
			else cout<<"Case #"<<(i+1)<<": RICHARD"<<"\n"; 
		}
	}
	return 0;
}
