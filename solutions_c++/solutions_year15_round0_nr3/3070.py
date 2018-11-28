#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <sstream>
#include <cmath>

#define For(i,a,n) for(ll i =a ; i < n ; ++i )
#define all(x) (x).begin(),(x).end()
#define n(x) (ll)(x).size()
#define pb(x) push_back(x)
#define fr first
#define sc second

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
const ll maxn = 10*1000+100;
const ll inf = 1000ll*1000ll*1000ll*1000ll*1000ll;
ll t;
ll l,x;
string s;

ll id(char ch){
	if(ch=='i')
		return 2;
	if(ch=='j')
		return 3;
	if(ch=='k')
		return 4;
	return 0;
}

ll mat[4][4]={ {1,	2,	3,	4},
		{2,	-1,	4,	-3},
		{3,     -4,    -1,      2},
		{4,	3,     -2,     -1}};

ll fx[9];
ll fp[9];
ll fs[9];
ll mu[maxn];
ll rmu[maxn];

ll sign(ll x){
	if( x < 0)
		return -1;
	return 1;
}

ll mult(ll i , ll j){
	return mat[abs(i)-1][abs(j)-1]*sign(i*j);
}
ll powq(ll x , ll y){
	ll v=x;
	ll ret=1;
	while(y){
		if(y%2)
			ret=mult(ret,v);
		v=mult(v,v);
		y/=2;
	}
	return ret;
}

int main()
{
	ios::sync_with_stdio(false);

	cin >> t;
	For(it,0,t){
		cin >> l >> x;
		cin >> s;
		cout << "Case #" << it+1 << ": ";
	
		mu[0]=1;
		For(i,0,n(s))
			mu[i+1]=mult(mu[i],id(s[i]));
		rmu[l]=1;
		for(int i = l-1; i>=0 ; i--)
			rmu[i]=mult(rmu[i+1],id(s[i]));

		if(powq(mu[l],x)!=-1){
			cout << "NO" << endl;
			continue;
		}

		For(i,0,9)
			fs[i]=fx[i]=fp[i]=inf;

		For(i,0,x+1)
			fx[4+powq(mu[l],i)]=min(fx[4+powq(mu[l],i)],i);
		For(i,0,l+1)
			fp[4+mu[i]]=min(fp[4+mu[i]],i);
		For(i,0,l+1)
			fs[4+rmu[i]]=min(fs[4+rmu[i]],l-i);

		bool flag = false;
		for(int i0 = -4 ; i0 <= 4 ; ++i0){
			if(i0==0)
				continue;
			for(int i1 = -4 ; i1 <= 4 ; ++i1){
				if(i1==0)
					continue;
				for(int k0 = -4 ; k0 <= 4 ; ++k0){
					if(k0==0)
						continue;
					for(int k1 = -4 ; k1 <= 4 ; ++k1){
						if(k1==0)
							continue;
						if(mult(i0,i1)==2 && mult(k0,k1)==4)
						{
							if(fx[4+i0] < inf && fx[4+k0] < inf &&
								       	fp[4+i1] < inf && fs[4+k1] < inf &&
								       	fx[4+i0]*l+fx[4+k0]*l+fp[4+i1]+fs[4+k1] <= x*l){
								flag=true;
							}
						}
					}
				}
		
			}
		}
		if(flag)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}

//
// el psy congroo
//

