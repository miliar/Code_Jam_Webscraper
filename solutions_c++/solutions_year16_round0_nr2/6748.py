#include <bits/stdc++.h>

using namespace std;


int main(void)
{
	ios::sync_with_stdio(false);

	int T;
	int tcase = 0;
	cin>>T;
	string answer;
	

	string s;	
		int cnt;
	
	while (++tcase<=T) {
		/// init
		// memset(visited, 0, sizeof(visited));
		cnt=0;
		
		/// input
		cin>>s;
		
		/// solution
		s=s+"+";
		
		for (int i=1;i<s.size();i++) {
			cnt+=s[i-1]!=s[i];
		}
		
		cout<<"Case #"<<tcase<<": ";
		
		/// answer
		cout<<cnt;
		
		cout<<endl;
	}
	
	return 0;
}

