#include <bits/stdc++.h>

using namespace std;

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int n;
		cin>>n;
		
		vector <int> v[n];
		set <string> S;
		
		for(int i=0; i<n; i++)
		{
			string s = "", t;
			cin>>t;
			t += '\0';
			
			char last = '\0';
			int cnt = 0;
			
			for(int j=0; j<t.size(); j++)
			{
				if(t[j] == last) cnt++;
				else
				{
					s += last;
					v[i].push_back(cnt);
					last = t[j];
					cnt = 1;
				}
			}
			
			S.insert(s);
		}
		
		cout<<"Case #"<<caso<<": ";
		
		if(S.size() != 1) cout<<"Fegla Won"<<endl;
		else
		{
			int ans = 0;
			
			for(int j=0; j<v[0].size(); j++)
			{
				vector <int> tmp;
				for(int i=0; i<n; i++)
					tmp.push_back(v[i][j]);
				
				sort(tmp.begin(), tmp.end());
				int m = tmp[n/2];
				for(int i=0; i<n; i++)
					ans += abs(tmp[i] - m);
			}
			
			cout<<ans<<endl;
		}
	}
  
	return 0;
}
