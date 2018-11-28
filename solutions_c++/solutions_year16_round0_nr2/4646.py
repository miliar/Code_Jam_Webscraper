#include <bits/stdc++.h>
using namespace std;

int t,len; string s,ideal; map<string,int> mp;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	freopen("pancakes.in","r",stdin);
	freopen("pancakes.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> s; len=s.length();
		ideal=""; mp.clear();
		for (int i=0;i<len;i++) ideal+='+';
		queue<pair<string,int>> q;
		q.push(make_pair(s,0));
		while (!q.empty()){
			pair<string,int> now=q.front(); q.pop();
			if (now.first==ideal){cout << now.second << "\n"; break;}
			for (int i=0;i<len;i++){
				string nxt=now.first;
				reverse(nxt.begin(),nxt.begin()+i+1);
				for (int j=0;j<=i;j++) nxt[j]=(nxt[j]=='-' ? '+' : '-');
				if (mp.count(nxt)) continue; mp[nxt]++;
				q.push(make_pair(nxt,now.second+1));
			}
		}
	}
}
