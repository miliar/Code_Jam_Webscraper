#include<bits/stdc++.h>
#define ll long long
#define whatis(x) cout<< #x << " is " << x << endl;

using namespace std;


inline string compress(string s){
	char cur = s[0];
	string comp = "";
	comp+=cur;

	for(int i = 0; i< s.size(); i++){
		if(s[i] != cur){
			comp+=s[i];
			cur = s[i];
		}
	}
	return comp;
}

inline char opposite(char x){return (x == '+'? '-': '+');}

string flip(string s, int index){
	//cout<<"flip a "<<s<<endl;
	int i = 0;
	int j = index;
	//whatis(i);
	//whatis(j);
	if(i == j ){
		s[i] = opposite(s[i]);
	//	whatis(i);
		//whatis(j);
	}
	else{
		while(i <= j){
			//whatis(i);
			//whatis(j);

			//whatis(s[i]);
			//whatis(s[j]);

			//cout<<"flip!"<<endl;
			char t = s[i];
			s[i] = opposite(s[j]);
			s[j] = opposite(s[i]);

			//whatis(s[i]);
			//whatis(s[j]);
			i++;
			j--;
			//whatis(s);

		}
	}
	return s;
}

ll solve(string s){
	string ans(s.size(), '+');
	if(s == ans)
		return 0;

	unordered_map<string, bool> seen;
	unordered_map<string, ll> depth;
	queue<string> q;

	ans = compress(ans);
	s = compress(s);

	for(int i = 0; i< s.size(); i++){
		string f = flip(s, i);
		f = compress(f);
		//whatis(f);
		if(seen.count(f) == 0){
			seen[f] = true;
			q.push(f);
			depth[f] = 1;
		}

		while(!q.empty()){
			string v = q.front(); q.pop();
			//whatis(v);
			if(v == ans) return depth[v];

			for(int i = 0; i < v.size(); i++){
				string w = flip(v, i);
				w = compress(w);
				//whatis(w);

				if(seen.count(w) == 0){
					seen[w] = true;
					q.push(w);
					depth[w] = depth[v] + 1;
					//whatis(depth[w]);
				}
			}
		}
	}
}

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int t = 1; t<=T; t++){
		string s;
		cin>>s;
		ll ans = solve(s);
		printf("case #%d: ",t);
		printf("%lld\n", ans);
	}
}
