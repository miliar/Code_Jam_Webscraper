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
	
	int t;
	string s, tmp;
	vector<string> list;
	vector<string> list_new_strings, list_tmp;
	
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> s;
		tmp = s[0];
		list_new_strings.pb(tmp);
		for (int k = 1; k < s.sz; k++)
		{
			for (int j = 0; j < list_new_strings.sz; j++)
			{
				tmp = s[k]+list_new_strings[j];
				list_tmp.pb(tmp);
				tmp = list_new_strings[j]+s[k];
				list_tmp.pb(tmp);
			}
			
			list_new_strings.clear();
			for (int j = 0; j < list_tmp.sz; j++)
				list_new_strings.pb(list_tmp[j]);
			list_tmp.clear();
		}
		
		for (int j = 0; j < list_new_strings.sz; j++)
			list.pb(list_new_strings[j]);
	
		sort(list.begin(), list.end());
		
		cout << "Case #" << i+1 << ": " << list[list.sz-1] << endl;
		list_new_strings.clear();
		list_tmp.clear();
		list.clear();
	}
	 
	
 	return 0;
}