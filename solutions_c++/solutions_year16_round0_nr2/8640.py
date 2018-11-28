#include <bits/stdc++.h>
using namespace std;
map<string,int> m;
void f(string x){
	int ans = 0;
	int maxv = 0;
	queue<pair<string,int> > q;
	q.push({x,0});
	while(!q.empty()){
		ans = max(ans,(int)q.size());
		string s = q.front().first;
		//cout<<s<<endl;
		int c = q.front().second;
		maxv = max(maxv,c);
		q.pop();
		int fl = 0;
		for(int i = 0;i<s.length();i++){
			if(s[i] == '-'){
				fl = 1;
				break;
			}
		}
		if(!fl){
			cout<<c<<endl;
			//cout<<ans<<" "<<maxv<<endl;
			return;
		}
		int n = s.length()-1;
		while(s[n]=='+')n--;
		string t = "";
		for(int i =0;i<=n;i++){
			t = "";
			for(int j = 0;j<=i;j++){
				t+=s[j];
			}
			reverse(t.begin(), t.end());
			for(int j = 0;j < t.size(); j++){
				if(t[j] == '+')t[j] = '-';
				else t[j] = '+';
			}
			for(int j = i+1;j <=n; j++){
					t+=s[j];
			}
			if(m[t])continue;
			m[t]=1;
			q.push({t,c+1});
		}
	}
}
void solve()
{
	m.clear();
	string s;
	cin>>s;
	string t ="";	
	int n = s.length()-1;
	while(s[n]=='+')n--;
	for(int i = 0;i <=n; i++){
		t+=s[i];
	}
	m[t]=1;
	f(t);
}
int main(int argc, char const *argv[])
{
	freopen("inp.txt","r",stdin);
	freopen("this.txt","w",stdout);
	int t;
	cin>>t;
	int i = 1;
	while(i<=t){
		printf("Case #%d: ",i);
		solve();
		i++;
	}
	//main2();
	return 0;
}