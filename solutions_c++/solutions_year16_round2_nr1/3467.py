#include<bits/stdc++.h>
using namespace std;

vector<string> dgts;

bool contains(string s, int dgt){
	string curr = dgts[dgt];
	map<char,int> mp;
	for(int i=0;i<s.size();i++){
		mp[s[i]]++;
	}
	for(int i=0;i<curr.size();i++){
		if(mp[curr[i]]==0)
			return false;
		mp[curr[i]]--;
	}
	return true;
}


string remove(string s, int dgt){
	string curr = dgts[dgt];
	map<char,int> mp;
	for(int i=0;i<curr.size();i++){
		mp[curr[i]]++;
	}
	string ans="";
	for(int i=0;i<s.size();i++){
		if(mp[s[i]]==0)
			ans+=s[i];
		else
			mp[s[i]]--;
	}
	return ans;
}

string recur(string live, int dgt, string ans){
	if(dgt==10)
		return "-1";
	
	if(live == "")
		return ans;
	
//	cout<<"trying "<<live<<" "<<dgt<<endl;
	if(contains(live, dgt)){
//		cout<<"found \n";
		string temp = recur(remove(live, dgt),dgt, ans+(char)(dgt+'0'));
		if(temp != "-1")
			return temp;
	}
	ans = recur(live, dgt+1, ans);
	
	
	return ans;
}

void eval(){
	string s;
	cin>>s;
	string ans = recur(s, 0, "");
	cout<<ans<<endl;
}

int main(){
	int t;
	//t=1;
	dgts = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<": ";
		eval();
	}
}
