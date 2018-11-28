#include <bits/stdc++.h>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>
#define MOD 1000000007
#define ll long long int
#define MAXINT 1000000001ll
#define SET(x,y) memset(x,y,sizeof(x));

using namespace std;

int C[10000];

ll work(ll n) {
	int i,j;
	ll m;
	for(i=0;i<=9;i++)	C[i]=0;
	for(i=1;;i++) {
		m=i*n;
		while(m) {
			C[m%10]++;
			m/=10;
		}
		for(j=0;j<=9;j++)
			if(!C[j])
				break;
		if(j==10)
			return i*n;
	}
}

int main() {
	int t,i,n;
	cin>>t;
	for(i=1;i<=t;i++) {
		cin>>n;
		cout<<"Case #"<<i<<": ";
		if(n==0)
			cout<<"INSOMNIA\n";
		else
			cout<<work(n)<<endl;
	}
	return 0;
}