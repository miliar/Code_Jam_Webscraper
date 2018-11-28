#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	int t;
	cin>>t;int cs=0;
	while(t--){
		cs++;
		string s;int k;
		cin>>s>>k;
		vector<bool>b;
		b.reserve(s.size());
		for (int i=0;i<s.size();i++)if (s[i]=='+')b.push_back(true);else b.push_back(false);
		int t=0,ans=0;
		while(t<=s.size()-k){
			bool f=0;
			while(t<s.size()&&b[t])t++;
			if (t>s.size()-k)break;
			int tt;
			for (int i=t;i<t+k;i++){
				b[i]=!b[i];
				if (!b[i]&&!f){
					f=1;
					tt=i;
				}
			}
			ans++;
			if (f)t=tt;
		}
		if (!b[s.size()-k]){
			for (int i=s.size()-k;i<s.size();i++)
				b[i]=!b[i];
			ans++;
		}
		bool f=1;
		for (int i=s.size()-k+1;i<s.size();i++)
			if (b[i]!=b[i-1]){f=0;break;}
		if (f)printf("Case #%d: %d\n",cs,ans);
		else printf("Case #%d: IMPOSSIBLE\n",cs);
	}
}
