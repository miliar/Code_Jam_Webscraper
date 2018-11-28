//Author: Mukul Chandel
#include<bits/stdc++.h>
using namespace std;
inline void fast_and_furious() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);
}

const int N=100005;
typedef long long ll;

int t,n;
set<char> st;
string s;

inline void refresh() {
	st.clear();
	s.clear();
}

inline void solve(int cse) {
	cin>>n;
	for(int i=1;n!=0 && i<=1000;i++){
		s=to_string(n*i);
		for(int j=0;j<s.length();j++){
			st.insert(s[j]);
		}
		if((int)st.size()==10){
			cout<<"Case #"<<cse<<": "<<s<<"\n";
			return;
		}
	}
	cout<<"Case #"<<cse<<": INSOMNIA\n"; 
}

int main() {
	fast_and_furious();
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	cin>>t;
	for(int i=1;i<=t;i++){
		solve(i);
		refresh();
  	}
	return 0;
}

