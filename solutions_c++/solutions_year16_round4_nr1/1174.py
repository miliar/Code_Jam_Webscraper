#include <bits/stdc++.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()
#define pb push_back
#define MOD 1000000007

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;

ll pw(ll b,int p, int m){
    ll a=1;
    while(p){
        if(p&1)
            a=(a*b)%m;
        b=(b*b)%m;
        p>>=1;
    }
    return a;
}

ll gcd(ll a, ll b){
    if(a<b)
        swap(a,b);
    if(!b)
        return a;
    return gcd(b,a%b);
}
bool grater_comp (pair<int,char> i,pair<int,char> j) { return (i.first>j.first); }

string solve(string s, int n){
	if(!n)
		return s;
	string r;
	f(i,s.size()){
		if(s[i]=='R'){
			r.pb(s[i]);
			r.pb('S');
		}
		if(s[i]=='S'){
			r.pb('P');
			r.pb(s[i]);
		}
		if(s[i]=='P'){
			r.pb(s[i]);
			r.pb('R');
		}
	}
	return solve(r,n-1);
}

void get(string &s, int st, int sz){
	int z=sz/2;
	if(z){
		get(s,st,z);
		get(s,st+z,z);
//		cout<<s.substr(st,z)<<" "<<s.substr(st+z,z)<<" "<< s.substr(st,z).compare(s.substr(st+z,z))<<"\n";
		if(s.substr(st,z).compare(s.substr(st+z,z))>0){
			f(i,z)
				swap(s[st+i],s[st+i+z]);
		}
	}

}
int check(string S, int r, int s, int p){
	f(i,S.size()){
		if(S[i]=='R')
			r--;
		if(S[i]=='S')
			s--;
		if(S[i]=='P')
			p--;
	}
	if(r || s || p)
		return 0;
	return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T,n,r,p,s;
	string S,m;
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<": ";
		cin>>n>>r>>p>>s;
		m.clear();
		S.clear();
		S.pb('R');
		S=solve(S,n);
		get(S,0,S.size());
		if(check(S,r,s,p)){
			m=S;
		}
		S.clear();
		S.pb('S');
		S=solve(S,n);
		get(S,0,S.size());
		if(check(S,r,s,p)){
			if(!m.size() || m.compare(S)>0)
				m=S;
		}
		S.clear();
		S.pb('P');
		S=solve(S,n);
		get(S,0,S.size());
		if(check(S,r,s,p)){
			if(!m.size() || m.compare(S)>0)
				m=S;
		}
		if(m.size())
			cout<<m<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
    }
    return 0;
}

