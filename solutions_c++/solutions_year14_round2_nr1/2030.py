#include <bits/stdc++.h>
using namespace std;

string gstr(string &s){
	if(s.size()<=1){
		string ans=s;
		s=string();
		return ans;
	}
	for(int i=1; s[i]; i++){
		if(s[i]!=s[0]){
			string ans=s.substr(0,i);
			s=s.substr(i);
			return ans;
		}
	}
	string ans=s;
	s=string();
	return ans;
}

bool verifi(vector<string> &vs){
	for(int i=1; i<(int)vs.size(); i++){
		if(vs[i][0]!=vs[i-1][0]) return false;
	}
	return true;
}

int mn(vector<string> &vs){
	int mn=105;
	for(int i=1; i<105; i++){
		int sm=0;
		for(int j=0; j<(int)vs.size(); j++){
			sm+=abs(i-(int)vs[j].size());
		}
		mn=min(mn, sm);
	}
	return mn;
}

int main(){
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t, n;
	cin>>t;
	for(int tc=1; tc<=t; tc++){
		cin>>n;
		vector<string> vs(n);
		for(int i=0; i<n; i++)
			cin>>vs[i];
		
		int ans=0;
		for(;;){
			vector<string> tmp;
			for(int i=0; i<(int)vs.size(); i++){
				string str=gstr(vs[i]);
				if(str.size()){
					tmp.push_back(str);
				}
			}
			if(tmp.size()==0) break;
			if(tmp.size()<vs.size()){
				ans=-1;
				break;
			}
			if(!verifi(tmp)){
				ans=-1;
				break;
			}
			ans+=mn(tmp);
		}
		
		cout<<"Case #"<<tc<<": ";
		if(ans==-1) cout<<"Fegla Won"<<endl;
		else cout<<ans<<endl;
	}
	

	return 0;
}
