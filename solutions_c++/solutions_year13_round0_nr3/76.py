#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)x.size())

using namespace std;

struct timer{
	time_t start;
	timer(){start=clock();}
	~timer(){cerr<<1.*(clock()-start)/CLOCKS_PER_SEC<<" secs"<<endl;}
};

typedef istringstream iss;
typedef long long ll;
typedef pair<int,int> pi;
typedef stringstream sst;
typedef vector<int> vi;

/*bool ispalin(ll n){
	int a[19],cur=0;
	while(n){
		a[cur++] = n%10;
		n/=10;
	}
	rep(i,cur/2){
		if(a[i] != a[cur-1-i])return 0;
	}
	return 1;
}*/

struct bigint{
	string s;
	bigint(){}
	bigint(string s):s(s){}
};

const bool operator < (const bigint& a,const bigint& b){
	return sz(a.s) < sz(b.s) || sz(a.s) == sz(b.s) && a.s < b.s;
}

bigint sq(const bigint& a){
	int n=sz(a.s);
	vi p(n);
	rep(i,n){
		rep(j,i+1){
			p[i]+=(a.s[j]-'0') * (a.s[i-j]-'0');
		}
	}
	bigint res;
	rep(i,n){
		res.s += (char)('0'+p[i]);
	}
	rep(i,n-1){
		res.s += (char)('0'+p[n-2-i]);
	}
	return res;
}

int main(){
	/*vector<ll> v;
	rep2(i,1,1000000010){
		if(i%100000000==0)cout<<i<<"/ 1B"<<endl;
		if(ispalin(i)){
			ll s=(ll)i*i;
			if(ispalin(s))cout<<i<<" ^2 = "<<s<<endl,v.pb(s);
		}
	}
	rep(i,sz(v))cout<<v[i]<<" ";cout<<endl;*/
	
	vector<bigint> v;
	v.pb(bigint("1"));
	v.pb(bigint("4"));
	v.pb(bigint("9"));
	
	rep2(dig,2,52){
		rep2(first,1,3){
			rep(center,dig%2?3:1){
				int one = (9 - first*first*2 - center*center)/2;
				int len = dig/2-1;
				//cout<<dig<<" "<<first<<" "<<center<<" : "<<one<<" "<<len<<endl;
				
				rep2(i,-2,len+1)rep2(j,i+1,len+1)rep2(k,j+1,len+1){
					if(i==-2){
						if(!(j==-1 && k==0))continue;
					}
					if(i==-1){
						if(j!=0)continue;
					}
					int used=(i>0)+(j>0)+(k>0);
					if(used > one)continue;
					bigint x;
					string s;
					s += (char)('0'+first);
					rep2(l,1,len+1){
						if(l==i || l==j || l==k)s+="1";
						else s+="0";
					}
					x.s += s;
					if(dig%2)x.s += (char)('0'+center);
					string t=s;
					reverse(t.begin(),t.end());
					x.s += t;
					//cout<<i<<" "<<j<<" "<<k<<" : "<<x.s<<endl;
					v.pb(sq(x));
				}
				
			}
		}
	}
	sort(v.begin(),v.end());
	
	rep(i,sz(v)-1){
		assert(v[i] < v[i+1]);
	}
	
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		
		bigint A,B;
		cin>>A.s>>B.s;
		cout<<upper_bound(v.begin(),v.end(),B) - lower_bound(v.begin(),v.end(),A)<<endl;
		
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
