#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
using namespace std;
typedef long long ll;
set<int> s;


bool f(string s)
{
	for (int i = 0; s[i]; i++)
		if (s[i]!='+')
			return false;
	return true;
}

int main()
{
    //ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;

	for (int tt = 0; tt<t; tt++)
	{
		string s;
		int ans = 0;
		cin >> s;
		int r = s.size()-1;
		while(r>=0&&s[r]=='+')
			r--;
		while (r>=0)
		{
			int i = 0;
			while (s[i] && s[i]=='+')
				i++;
			//cout << i << " " << r << " " << ans << endl;
			if (i)
			{
			//	cout << "i"<< endl;
				ans++;
				for (int j = 0; j<i; j++)
					s[j]='-';
				
			}
			for (int i = 0; i<=r; i++)
				if (s[i]=='-')
					s[i]='+';
				else
					s[i]='-';
			ans++;
		//	cout << s << endl;
			reverse(s.begin(),s.begin()+r+1);
		//	cout << s << endl;
			while (r>=0&&s[r]=='+')
				r--;
		}
		cout << "Case #"<<tt+1<< ": " << ans << endl;
	}
	return 0;   
}									  