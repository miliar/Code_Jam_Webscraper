#include<bits/stdc++.h>

using namespace std;

string s;

int main()
{
	int t;
	
	freopen("B-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		int cnt=0;
		
		cin >> s;
		
		cout << "Case #" << tt+1 << ": ";
		
		if(s.size()==1)
		{
			if(s[0]=='-')
				cout << 1 << endl;
			else
				cout << 0 << endl;
				
			continue;
		}
		
		for(int i=1;i<s.size();i++)
			if(s[i]!=s[i-1])
				cnt++;
				
		if(s[s.size()-1]=='-')
			cnt++;
			
		cout << cnt << endl;
	}
	
	return 0;
}
