// AUTHOR: ARVIND NAIR

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pi;
typedef vector<int> vi;

#define TEST  int test_case; scanf("%d",&test_case); while(test_case--)
#define RT fprintf(stderr, "\nTIME = %lf\n", 1.0 * clock()/CLOCKS_PER_SEC);
#define rep(a,c)   for ( int (a)=0; (a)<(c); (a)++)
#define repn(a,b,c)  for ( int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for (  int (a)=(b); (a)>=(c); (a)--)
#define FOR(arr) for(auto &i:arr)
#define all(v) (v).begin(),(v).end()
#define fi  first
#define se  second
#define pb push_back
#define mp make_pair
#define EPS (double)(1e-9)
#define MOD 1000000007
#define M(x,i) memset(x,i,sizeof(x))
#define trace(x)    cout<<#x<<" is "<<x<<"\n"
#define sz(x) (int)(x.size())
#define si(n) scanf("%d",&n)
#define gi(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define gll(n) printf("%lld\n",n)

map<string,int> seen;

string transform(string x) {

	rep(i,sz(x))
	 if(x[i]=='+')
	 	x[i]='-';
	 else
	 	x[i]='+';

	 return x;
}

bool check(string x) {

	int cnt=0;

	rep(i,sz(x))
	 if(x[i]=='+')
	 	++cnt;

	 return (cnt==sz(x));
}

int main() {

freopen("inp.in","r",stdin);
freopen("op.out","w",stdout);	

int t;  si(t);   

repn(test,1,t) {

	seen.clear();

	queue<pair<string,int>> Q;
	int ans;

	string s; cin>>s;
	Q.push({s,0});
    seen[s]=1;

	while(!Q.empty()) {

    s=Q.front().fi;
    int n=Q.front().se;

    Q.pop();

    if(check(s)) {

    	ans=n;
    	break;
    }

    repn(i,1,sz(s)) {


    	string p=s.substr(0,i);
    	reverse(all(p));
    	string x=transform(p)+s.substr(i);
    	if(seen[x]!=1)
    	Q.push({x,n+1}),seen[x]=1;
    }

	}

	printf("Case #%d: %d\n",test,ans);
}
     
return 0;
}
