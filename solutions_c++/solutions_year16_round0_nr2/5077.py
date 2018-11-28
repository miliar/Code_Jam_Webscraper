#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

#define LL long long

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		string str;
		cin >> str;
		int ans = 0;
		int s = 0;
		if(str[s] == '-')
		{
			ans++;
			while(s != str.length() && str[s] == '-')
			{
				s++;
			}
		}
		while(s + 1 < str.length())
		{
			if(str[s] == '+' && str[s+1] == '-')
			{
				ans = ans + 2;
			}
			s++;
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
