#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
int main()
{
	int t,i;
	scanf("%d",&t);
	for( i=1;i<=t;i++) {
		ll n;
		scanf("%llu",&n);
		set <int> s;
		if(n==0) {
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		ll j,p;
		for(j=n;s.size()<10;j+=n) {
			p=j;
			while(p!=0) {
				s.insert(p%10);
				p=p/10;
			}
		}
		cout<<"Case #"<<i<<": "<<j-n<<endl; 
	}
	return 0;
}
