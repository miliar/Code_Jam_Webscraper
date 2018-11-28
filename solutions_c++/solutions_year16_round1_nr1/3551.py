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
#define FORI(i,b,a) for(int i = b ; i >= a ; i--)

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		string str;
		cin >> str;
		int n = str.length();
		if(n == 1)
		{
			cout << "Case #" << tc << ": " << str << endl;
			continue;
		}
		vector <char> arr(n);
		arr[1] = str[1];
		FOR(i,2,n)
		{
			arr[i] = max(arr[i-1], str[i]);
		}
		string ans = "";
		FORI(i,n-1,1)
		{
			if(str[i] == arr[i] && str[i] >= str[0])
			{
				ans = ans + str[i];
			}
		}
		ans = ans + str[0];
		FOR(i,1,n)
		{
			if(str[i] != arr[i] || str[i] < str[0])
			{
				ans = ans + str[i];
			}
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
