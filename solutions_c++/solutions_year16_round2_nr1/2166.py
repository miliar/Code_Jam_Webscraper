#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
string nu = "ZOWRUFXSGNINE";
string nn[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int test = 1;
void solve()
{
	vector<int> ans;
	cout << "Case #" << test++ << ": ";
	string s; cin >> s;
	for( int i = 0 ; i < 9 ; i++ )
	{
		if(i%2==1) continue;
		char ch = nu[i];
		string::iterator it;
		for(it=s.begin();it!=s.end();it++)
		{
			if((*it)==ch) 
			{
				string &ss = nn[i];
				for( int j = 0 ; j < ss.length() ; j++ )
				{
					char cc = ss[j];
					for( int k = 0 ; k < s.length() ; k++ )
					{
						if(s[k] == cc )
						{
							s[k] = '-';
							break;
						}
					}
				}
				ans.push_back(i);
			}
		}
	}
	for( int i = 0 ; i <= 12 ; i++ )
	{
		if(i<9 && i%2==0) continue;
		char ch = nu[i];
		string::iterator it;
		for(it=s.begin();it!=s.end();it++)
		{
			if((*it)==ch) 
			{
				string &ss = nn[i<=9?i:9];
				for( int j = 0 ; j < ss.length() ; j++ )
				{
					char cc = ss[j];
					for( int k = 0 ; k < s.length() ; k++ )
					{
						if(s[k] == cc )
						{
							s[k] = '-';
							break;
						}
					}
				}
				ans.push_back(i);
			}
		}
	}
	sort(ans.begin(),ans.end());
	for( int i = 0 ; i < ans.size() ; i++ ) cout << ans[i];
	cout << endl;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("aoutll.out","w",stdout);
	int t; cin>>t;
	while(t--)
	{
		solve();
	}
	return 0;
}