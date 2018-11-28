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

void set_insert(int n, set<int> &st){
	if(n==0){
		st.insert(0);
		return;
	}
	while(n){
		st.insert(n%10);
		n/=10;
	}
	
}

int main(void){
	ios_base::sync_with_stdio(0);
	freopen("out","w",stdout);
	freopen("in","r",stdin);
	int tst;
	cin>>tst;
	repi(ks,1,tst+1){
		int n;
		cin>>n;
		set<int> st;
		ll t = 0;
		repi(i,1,91){
			t = 1LL*n*i;
			set_insert(t,st);
			if(st.size()==10)break;
		}
		if(st.size()==10){
			cout<<"Case #"<<ks<<": "<<t<<endl;
		}else{
			cout<<"Case #"<<ks<<": "<<"INSOMNIA"<<endl;
		}
	}
	return 0;
}
