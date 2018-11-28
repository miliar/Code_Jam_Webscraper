#include <iostream>
#include <stdio.h>
#include <algorithm>
#define FOR(i,n) for(ll i=0;i<n;i++)
#define FR(i,k,n) for(ll i=k;i<n;i++)
#define size 10000007
typedef long long int ll;
using namespace std;
char s[size];
int main() {
	ll t,k,sum,sm;
	freopen("r.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	FR(q,1,t+1){
		cout<<"Case #"<<q<<": ";
		k=0;cin>>sm;
		FOR(i,sm+1)cin>>s[i];
		sum = s[0]-48;//cerr<<"\ninitial "<<sum;
		FR(i,1,sm+1){
			if(sum<i && s[i]!='0'){k+=(i-sum);sum+=(i-sum);/*cerr<<"\nvalue added by "<<sum;*/}
			if(s[i]!='0')sum+=((s[i]-48));
		}
		cerr<<q<<": "<<sum<<"\n";
		if(sm>sum)k++;
		cout<<k<<"\n";
	}
	return 0;
}
