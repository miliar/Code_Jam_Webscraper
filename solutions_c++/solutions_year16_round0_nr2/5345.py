#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define pb(x) push_back(x)
#define mp(i,j) make_pair(i,j)
#define MAXN 100010
#define MOD 1000000007

//map <string,bool> vis;
//queue <pair<string,ll> > q;
string s;
//string ns;

ll rec(ll i,ll type)
{
	ll j;

	for(j=i;j>=0;j--) {
		if(type==0) {
			if(s[j]=='-') break;
		} else if(type==1) {
			if(s[j]=='+') break;
		}
	}

	if(j<0) return 0;
	else {
		return (1 + rec(j,1-type));
	}
}

int main()
{
	ll c,t,move,len,i,j;

	scanf("%lld", &t);

	for(c=1;c<=t;c++) {
		cin>>s;
		len = s.length();

		printf("Case #%lld: %lld\n", c,rec(len-1,0));
		
//		cout<<len<<endl;
/*		q.push(mp(s,0));

		vis[s] = true;

		while(!q.empty()) {
			s = q.front().first;
			move = q.front().second;
			q.pop();
//			cout<<s<<" "<<move<<endl;
			for(i=0;i<len;i++) if(s[i]=='-') break;

			if(i==len) break;

			for(i=0;i<len;i++) {
				ns = s;
				for(j=0;j<=i;j++) {
					if(s[i-j]=='+') {
						ns[j] ='-';
					} else if(s[i-j]=='-') {
						ns[j] ='+';
					}
				}
				if(vis[ns]==false) {
				//	cout<<"pushing: "<<ns<<endl;
					vis[ns] = true;
					q.push(mp(ns,move+1));
				}
			}
		}

		printf("Case #%lld: %lld\n", c,move);

		while(!q.empty()) q.pop();
		vis.clear();
*/		
	}

	return 0;
}
