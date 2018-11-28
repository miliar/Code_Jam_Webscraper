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


vector<pair<string, vector<int> > > ans;

ll get(string str, int pos)
{
	ll ans = 0;
	ll prod = 1;
	for (int i = str.size() - 1; i >= 0; --i)
	{
		ans += (str[i] - '0')*prod;
		prod *= pos;
	}
	return ans;
}

int n, j;

void check(int a)
{
	if (ans.size() == j)
		exit(0);
	string str;
	for (int i = 0; i < n; ++i)
	{
		if (a & (1 << i))
		{
			str += '1';
		}
		else
		{
			str += '0';
		}
	}
	if (str[0] != '1' || str.back() != '1')
		return;
	vector<int> tmp;
	for (int i = 2; i <= 10; ++i)
	{
		ll cur = get(str, i);
		for (int j = 2; j < min(150ll, cur); ++j)
		{
			if ((cur % j) == 0)
			{
				tmp.push_back(j);
				break;
			}
		}
	}

	if (tmp.size() == 9)
	{
		ans.push_back(make_pair(str, tmp));
		cout << str << ' ';
		for (int i = 0; i < tmp.size(); ++i)
		{
			cout << tmp[i] << ' ';
		}
		cout << endl;
	}

}


int main(){
#ifdef _CONSOLE 
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 

	
	int test;
	cin >> test;
	
	cin >> n >> j;

	int msk = 0;
	cout << "Case #1:\n";
	for (int i = 0; i < (1 << n); ++i)
	{
		check(i);
	}

	



	return 0;
}

