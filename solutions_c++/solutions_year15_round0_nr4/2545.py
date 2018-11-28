#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define rep(i,a,b) for(i=a; i<=b; i++)

int main()
{
	ios_base::sync_with_stdio(false);
	ll test, t; cin>>test;
	rep (t,0,test-1){
		int x,r,c; cin>>x>>r>>c;
		int res = -1;
		if (x == 1) res = 1;
		else if (x == 2){
			if ( (r*c) % 2 == 1 || (r * c < 2)) res = 0;
			else res = 1;
		}
		else if (x == 3){
			if (r*c == 6) res = 1;
			else if (r*c == 9) res = 1;
			else if (r*c == 12) res = 1;
			else if (r*c == 16) res = 0;
			else res = 0;
		}
		else if (x == 4){
			if (r*c == 12) res = 1;
			else if (r*c == 16) res = 1;
			else res = 0;
		}
		if (res == 0) cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
		else if (res == 1) cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
		else cout<<"JHINGA LA LA HU##########################";
	}
	return 0;
}
