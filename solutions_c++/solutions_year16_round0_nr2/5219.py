#include <iostream> 
#include <vector> 
#include <string> 
#include <algorithm> 
#include <sstream> 
#include <set> 
#include <map> 
#include <queue> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <bitset> 
#include <unordered_map> 
#include <unordered_set> 

using namespace std;
typedef long long ll;

int getlast(string str)
{

	int ans = 0;
	
	while (1)
	{
		int ptr = 0;
		while (ptr < str.size() && str[ptr] == '+')
		{
			ptr++;
		}
		if (ptr == str.size())
			break;
		if (ptr != 0)
		{
			ans++;
		}
		ans++;
		while (ptr < str.size() && str[ptr] == '-')
		{
			str[ptr] = '+';
			ptr++;
		}	
		if (ptr == str.size())
			break;
	}
	return ans;
}

int main(){
#ifdef _CONSOLE 
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 

	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		string str;
		cin >> str;
		
		int ans = getlast(str);
		printf("Case #%d: %d\n", t, ans);
	}
	



	return 0;
}

