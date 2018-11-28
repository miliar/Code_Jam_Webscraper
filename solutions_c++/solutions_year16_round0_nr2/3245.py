#include<bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi > vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long ll;
typedef vector<pii > vpii;
typedef vector<ll> vll;

#define mp make_pair
#define pb push_back
#define eps 1e-9
#define all(a) (a).begin(),(a).end()
#define len(a) int((a).size())
#define  mem(a,n) memset(a,n,sizeof(a))
#define rep(i,n) for(int i=0;i<(n);i++)
#define repi(i,a,n) for(int i=(a);i<(n);i++)
#define repr(i,a,n) for(int i=(n);i>=(a);i--)
#define inf 1e9



int main(void){
	ios_base::sync_with_stdio(0);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tst;
	cin>>tst;
	repi(ks,1,tst+1){
		string s;
		cin>>s;
		string t="";
		rep(i,len(s)){
			if(i>0 && s[i]==s[i-1])continue;
			t.pb(s[i]);
		}
		int ans = len(t)-(t[len(t)-1]=='+');
		cout<<"Case #"<<ks<<": "<<ans<<endl;
	}
	return 0;
}
