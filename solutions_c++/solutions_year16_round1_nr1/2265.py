#include <bits/stdc++.h>
using namespace std;

int t,len; string s,ss;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	freopen("lastword.in","r",stdin);
	freopen("lastword.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> s; len=s.length();
		ss="";
		for (int i=0;i<len;i++){
			if (!i||s[i]<ss[0]) ss+=s[i];
			else ss=s[i]+ss;
		}
		cout << ss << "\n";
	}
}
