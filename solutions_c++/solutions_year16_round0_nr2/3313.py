#include <bits/stdc++.h>
using namespace std;
string flip(string str,int k){
	int n = str.length();
	assert(k<=n);
	reverse(str.begin(),str.begin()+k);
	for(int i=0;i<k;i++)
		str[i] = (str[i] == '+')?'-':'+';
	return str;	 
}

map<string,int> mp;
vector<int> g[1000008];
string s[10000008];
int ind = 1;

void rec(string str){
	int n = str.length();
	mp[str] = ind;
	s[ind] = str;
	ind++;
	for(int i=1;i<=n;i++){
		string t = flip(str,i);
		if(mp.find(t) != mp.end()){
			g[mp[t]].push_back(mp[str]);
			g[mp[str]].push_back(mp[t]);
		}
		else rec(t);
	}	
}
bool allPlus(int u){
	int n = s[u].length();
	for(int i=0;i<n;i++)
		if(s[u][i] == '-')return false;
	return true;
}
int main(int argc, char const *argv[])
{
	int T,p=1;
	string str;
	cin>>T;
	int k = 1;
	while(T--){
		cin>>str;
		ind = 1;
		rec(str);
		//cout<<ind<<endl;
		// for(int i=1;i<ind;i++){
		// 	cout<<s[i]<<" ==> ";
		// 	for(int j=0;j<g[i].size();j++){
		// 		cout<<s[g[i][j]]<<" ";
		// 	}
		// 	cout<<endl;
		// }
		queue<pair<int,int> > q;
		vector<bool> visited(ind,false);
		q.push(make_pair(1,0));
		int ans = 0;
		while(!q.empty()){
			int u = q.front().first;
			int w = q.front().second;
			//cout<<s[u]<<" "<<w<<endl;
			q.pop();
			visited[u] = true;
			if(allPlus(u)){
				ans = w;
				break;
			}
				
			int size = g[u].size();
			for(int i=0;i<size;i++){
				int v = g[u][i];
				if(!visited[v])
					q.push(make_pair(v,w+1));
			}
		} 
		cout<<"Case #"<<k++<<": "<<ans<<endl;
		mp.clear();
		for(int i=1;i<=ind;i++)
			g[i].clear();
	}
	return 0;
}