#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<cmath>
#include<cstdlib>
#include<complex>
#include<sstream>
#include<iomanip>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb(x) push_back(x)
#define ll long long
#define VI vector<int>

ll getInBase(ll k, int b){
	ll res = 0, p = 1;
	rep(i,16){
		if((k>>i)&1)
			res += p;
		p*=b;
	}
	return res;
}

ll isPrime(ll q){
	for(ll i=2;i*i<=q;i++)
		if(q%i == 0)
			return i;
	return -1;
}

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	rep(g,t){
		int n, m;
		cin >> n >> m;
		ll st = 1;
		st <<= (n-1);
		st++;
		int cnt = 0;
		cout << "Case #" << g+1 << ":" << endl;
		for(ll i = st;cnt < m;i+=2){
			VI v;
			For(j,2,11){
		//		cout << getInBase(i,j) << endl;
				v.pb(isPrime(getInBase(i,j)));
				if(v.back() == -1)
					goto hell;
			}
			rep(j,n)
				cout << ((i>>(n-j-1))&1);
			rep(j,v.size())
				cout << " " << v[j];
			cout << endl;
			cnt++;
			hell:;
		}

	}
	return 0;
}
