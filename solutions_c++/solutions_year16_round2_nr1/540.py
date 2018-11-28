#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

class item
{
public :
	char val, dist;
	string str;
	item(char val1, char dist1, string str1){
		val = val1;
		dist = dist1;
		str = str1;
	}

};
int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	vector <item> vec;
	vec.push_back(*(new item('0', 'Z', "ZERO")));
	vec.push_back(*(new item('2', 'W', "TWO")));
	vec.push_back(*(new item('4', 'U', "FOUR")));
	vec.push_back(*(new item('6', 'X', "SIX")));
	vec.push_back(*(new item('8', 'G', "EIGHT")));
	vec.push_back(*(new item('3', 'H', "THREE")));
	vec.push_back(*(new item('5', 'F', "FIVE")));
	vec.push_back(*(new item('7', 'V', "SEVEN")));
	vec.push_back(*(new item('9', 'I', "NINE")));
	vec.push_back(*(new item('1', 'O', "ONE")));
	

	int t;
	cin >> t;

	for (int z = 1; z <= t; z++)
	{
		string str;
		cin >> str;
		int mp[26];
		memset(mp, 0, sizeof(mp));
		string res = "";

		for (int i = 0; i < str.length(); i++)
		{
			mp[str[i] - 'A']++;
		}

		for (int i = 0; i < vec.size(); i++)
		{
			while (mp[vec[i].dist - 'A'] > 0)
			{
				res += vec[i].val;
				for (int j = 0; j < vec[i].str.length(); j++)
				{
					mp[vec[i].str[j] - 'A']--;
				}
			}
		}
		sort(res.begin(), res.end());

		cout << "Case #" << z << ": " << res << endl;
	}
	return 0;
}