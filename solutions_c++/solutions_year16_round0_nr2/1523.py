#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int tnum=1; tnum<=T; ++tnum)
	{
		string s;
		cin >> s;
		cout << "Case #"<<tnum<<": ";
		int p=0, m=0;
		if(s[0]=='-')
			m++;
		else p++;
		int ans=0;
		for(int i=1; i<s.length(); ++i)
			if(s[i]=='+'){
				if(m>0)
					ans++;
				m=0; p=1;
			}else{
				if(p>0)
					ans++;
				p=0; m=1;
			}
		if(m>0)
			++ans;
		cout << ans << endl;
	}
}