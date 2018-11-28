#include <bits/stdc++.h>
 
using namespace std; 
 
typedef long long ll; 
typedef pair<int, int> pii;
 
#define MOD 1000000007
#define INF 1000000000
#define pb push_back 
#define sz size() 
#define mp make_pair

#define f(i,a,b) for(i=a;i<b;i++)

int main()
{
	
	bool ok;
	int t, pos, ans, ind;
	string s, s_tmp;
	
	cin >> t;
	for(int k = 0; k < t; k++)
	{
		cin >> s;
		
		ans = 0;		
		for (int j = s.sz; j > 0; j--)
		{	
			pos = j-1;
			ok = false;
			if (s[pos] == '-')
			{
				if (s[0] == '+')
				{
					ans++;
					
					ind = 0;
					while (ind < s.sz && s[ind] != '-')
						ind++;
					
					for (int i = 0; i < ind; i++)
					{
						s[i] = '-';
					}
				}
			
				for (int i = pos; i >= 0; i--)
				{
					if (s[i] == '-')
						s_tmp.pb('+');
					else
						s_tmp.pb('-');
				}
				s_tmp[pos] = '+';
				
				ans++;
					
				for (int i = pos+1; i < s.sz; i++)
					s_tmp.pb('+');
				
				s = s_tmp;
				s_tmp.clear();
			}
		}
		
		if (s[0] == '-')
			ans++;
		
		cout << "Case #" << k+1 << ": " << ans << endl;
	}
	
 	return 0;
}