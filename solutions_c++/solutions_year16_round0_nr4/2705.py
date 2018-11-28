#include<bits/stdc++.h>
#define mod 1000000007
#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define ff first
#define ss second
#define big 100000000000000000
using namespace std;

ll tc,k,c,s,i,j;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>k>>c>>s;
		cout<<"Case #"<<t<<": ";
		for(i=1;i<=s;i++)
			cout<<i<<" ";
		cout<<"\n";
	}
	return 0;
}

