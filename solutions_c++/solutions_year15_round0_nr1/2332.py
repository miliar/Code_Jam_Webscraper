#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <hash_map>
#include <unordered_set>

using namespace std;
typedef long long ll;


int main(){
	freopen("A-large (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n;
		cin >> n;
		string str;
		cin >> str;
		int add = 0;
		int cur = 0;
		for (int i = 0; i <= n; ++i)
		{
			if (cur < i)
			{
				add += (i - cur);
				cur = i;
			}
			cur += str[i] - '0';
		}
		cout <<"Case #"<<t<<": "<< add << endl;
	}


	return 0;
}