#include <bits/stdc++.h>
using namespace std;
#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))
#define abs(x) ((x) < 0 ? -(x) : (x))


int t;
string s_inp,s,tmp_s;
int ans,tmpans;

int main()
{
	cin.sync_with_stdio(0);
	//cin.tie(0);
	cin >> t;
	for (int i=1;i<=t;++i) {
		cin >> s_inp;
		tmp_s.clear();
		for (int j=0;j<s_inp.size();++j) {
			if (j==0 || s_inp[j]!=s_inp[j-1]) tmp_s.push_back(s_inp[j]);
		}
		s_inp=tmp_s;
		//cout << s_inp << '\n';
		//----
		
		s=s_inp;
		s.push_back('+');
		tmpans=0;
		for (int j=0;j<s.size()-1;++j) {
			if (s[j]!=s[j+1]) {
				if (s[j]=='-') ++tmpans;
				else {
					s[j+1]='+';
					tmpans+=2;
				}
			}
		}
		ans=tmpans;
		
		//----
		
		s=s_inp;
		s.push_back('-');
		tmpans=1;
		for (int j=0;j<s.size()-1;++j) {
			if (s[j]!=s[j+1]) {
				if (s[j]=='+') ++tmpans;
				else {
					s[j+1]='-';
					tmpans+=2;
				}
			}
		}
		ans=min(ans,tmpans);
		
		//----
		
		s.clear();
		for (int j=s_inp.size()-1;j>=0;--j) {
			if (s_inp[j]=='+') s.push_back('-');
			else s.push_back('+');
		}
		s.push_back('+');
		tmpans=1;
		for (int j=0;j<s.size()-1;++j) {
			if (s[j]!=s[j+1]) {
				if (s[j]=='-') ++tmpans;
				else {
					s[j+1]='+';
					tmpans+=2;
				}
			}
		}
		ans=min(ans,tmpans);
		
		//----
		
		s.clear();
		for (int j=s_inp.size()-1;j>=0;--j) {
			if (s_inp[j]=='+') s.push_back('-');
			else s.push_back('+');
		}
		s.push_back('-');
		tmpans=2;
		for (int j=0;j<s.size()-1;++j) {
			if (s[j]!=s[j+1]) {
				if (s[j]=='+') ++tmpans;
				else {
					s[j+1]='-';
					tmpans+=2;
				}
			}
		}
		ans=min(ans,tmpans);
		
		//----
		
		cout << "Case #" << i << ": " << ans << '\n';
	}
	return 0;
}

