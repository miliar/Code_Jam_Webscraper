#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
string numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int vis[2005];
bool check(string s, int x){
	set<int> vis2;
	int i;
	for(i = 0; i < numbers[x].length(); ++i){
		int j;
		for (j = 0; j < s.length(); ++j)
		{
			if(s[j] == numbers[x][i] && !vis[j] && vis2.count(j) == 0) {vis2.insert(j); break;}
		}
		if(j == s.length()) return false;

	}
	for (auto it: vis2)
	{
		vis[it] = 1;
	}
	return true;  
}
bool done(string s){
	for (int i = 0; i < s.length(); ++i)
	{
		if(!vis[i]) return false;
	}
	return true;
}
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	int t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		stringstream soll; 
		string s; cin>>s;
		vector<int> sol;
		int rep[15];
		int k = 0;
		while(true){
		
			soll.str("");
			memset(vis, 0, sizeof vis); //memset(rep, 0, sizeof rep); 
			sol.clear();
			for(int i = k; i < 10 + k; ++i){
				//cout<<i%10<<" "<<k<<endl;
				for(int j = 0; j < 670; ++j)
					if(check(s, i % 10)){
						//cout<<s<<" "<<i<<endl;
						sol.push_back(i % 10);
						//rep[i]++;
					}
			}
			//cout<<sol.size()<<endl;
			sort(sol.begin(), sol.end());
			for(auto it: sol) soll<<it;
			if(done(s)) break;
			++k; k %= 10;
		}
		cout<<"Case #"<<(i + 1)<<": "<<soll.str()<<"\n";;
	}
	return 0;
}
