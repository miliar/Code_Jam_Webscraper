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

ll getlast(ll num)
{
	set<int> s;
	stringstream stream;
	stream<<num;
	string str;
	stream>>str;
	for (int i = 0; i<str.size(); ++i)
	{
		s.insert(str[i] - '0');
	}
	ll i = 1;
	while (s.size() != 10)
	{
		i++;
		ll tmp = num * i;
		stringstream stream;
		string str;
		stream<<tmp;
		stream>>str;
		for (int i = 0; i<str.size(); ++i)
		{
			s.insert(str[i] - '0');
		}
	}
	return num * i;
}

int main(){
#ifdef _CONSOLE 
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 

	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		ll num;
		cin >> num;
		if (num == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		
		ll ans = getlast(num);
		printf("Case #%d: %lld\n", t, ans);
	}
	



	return 0;
}

