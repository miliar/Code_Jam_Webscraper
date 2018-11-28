#include<bits/stdc++.h>
#define LOCAL
#define DEBUG
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define sf(n) scanf("%f",&n)
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
#define pln(n) cout<<n<<endl
#define pnl() printf("\n")
#define pls(n) cout<<n<<" "
#define pl(n) cout<<n
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define FORR(i,j,n) for(i=j;i>=n;i--)
#define SORT(n) std::sort(n.begin(),n.end())
#define FILL(n,a) std::fill(n.begin(),n.end(),a)
#define ALL(n) n.begin(),n.end()
#define rsz resize
#define pb push_back
#define MAXINT std::numeric_limits<int>::max()
#define MININT std::numeric_limits<int>::min()
#define getchar gc
#define putchar pc
#define iOS std::ios_base::sync_with_stdio(false)
#define endl "\n"
#ifdef DEBUG
    #define debug(x) cout << #x << " = " << x << endl
#else
    #define debug(x)
#endif
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef pair<int,int> pii;
 
/**************** TEMPLATE ENDS HERE *************************/
ll getVal(string s,int dig,int base) {
	int i;
	ll ret=0LL;
	ll mult=1LL;
	FOR(i,0,dig-1) {
		if(s[i]=='1') ret+=mult;
		mult*=ll(base);
	}
	//if(s=="110001") exit(0);
	return ret;
}
int isPrime(ll num) {
	int i;
	int s=sqrt(num);
	if(num==0LL || num==1LL) assert(false);
	if(num==2LL) return 0;
	if(num%2LL == 0LL) return 2;
	
	for(i=3;i<=s;i++) {
		if(num%ll(i) == 0LL) return i;
	}
	return 0;
}
pair< bool, pair<string, vector<int> > > getAns(int num,int dig) {
	int t,i,divisor,base;
	//debug(r);
	num<<=1;
	num++;
	num|=(1<<(dig-1));
	string s;
	s.resize(dig);
	t=1;
	i=0;
	while(t<=num) {
		if(t&num) {
			s[i]='1';
		}
		else {
			s[i]='0';
		}
		t<<=1;
		i++;
	}
	pair< bool, pair<string, vector<int> > > ret;
	ret.second.first=s;
	if(s=="111111") {
		debug(num);
	}
	FOR(base,2,10) {
		ll val=getVal(s,dig,base);
		divisor=isPrime(val);
		if(num==63) {
			debug(base);
			debug(val);
			debug(divisor);
		}
		if(divisor==0) {
			ret.first=false;
			return ret;
		}
		else {
			ret.second.second.push_back(divisor);
		}
	}
	ret.first=true;
	assert(ret.second.second.size()==9);
	return ret;
}
int main() {
	int t,tt,n,r,i;si(t);
	FOR(tt,1,t) {
		si(n);si(r);
		int up=(1<<(n-2))-1;
		pair< bool, pair<string, vector<int> > > temp;
		vector< pair< string, vector<int> > > ans;
		FOR(i,0,up) {
			temp=getAns(i,n);
			if(temp.first) {
				ans.push_back(temp.second);
				r--;
				if(r==0) break;
			}
		}
		assert(r==0);
		cout<<"Case #"<<tt<<": "<<endl;
		for(auto it:ans) {
			reverse(it.first.begin(),it.first.end());
			cout<<it.first<<" ";
			for(auto it2:(it.second)) ps(it2);
			cout<<endl;
		}
	}
	return 0;
}
