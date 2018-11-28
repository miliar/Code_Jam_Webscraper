#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;++i)
#define repi(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define vi vector<int>
#define sc(a) scanf("%d",&a)
#define pb(a) push_back(a)
#define pr(a) printf("%d",a)
#define prn(a) printf("%d\n",a)
#define scll(a) scanf("%lld",&a)
#define prll(a) printf("%lld",a)
#define prlln(a) printf("%lld\n",a)
int t;
string s;
int main() {
	// your code goes here
	
	int t;
	cin>>t;
	for(int tt=1;tt<=t;++tt) {
		cout<<"Case #"<<tt<<": ";
		cin>>s;
		string s2;
		for(int i=0,j=0;i<s.size();) {
			while(j < s.size() && s[j]==s[i]) ++j;
			s2.pb(s[i]);
			i = j;
		}
		if(s2[s2.size()-1] == '+')s2.pop_back();
		cout<<s2.size()<<endl;
	}
	return 0;
}