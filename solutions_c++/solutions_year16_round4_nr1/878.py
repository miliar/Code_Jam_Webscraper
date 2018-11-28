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



string to[3] = { "RS", "PR", "PS" };
int getInd(char c)
{
	if (c == 'R')
		return 0;
	if (c == 'P')
		return 1;
	if (c == 'S')
		return 2;
}

string check(int n, int r, int p, int s, string st)
{
	for (int i = 0; i < n; ++i)
	{
		string next;
		for (int i = 0; i < st.size(); ++i)
		{
			int ind = getInd(st[i]);
			next += to[ind];
		}
		st = next;
	}
	int count[3] = { 0,0,0 };
	for (int i = 0; i < st.size(); ++i)
	{
		count[getInd(st[i])] ++;
	}
	if (count[0] != r || count[1] != p || count[2] != s)
		return "";
	else
		return st;
}

string ans;

void mysort(int n)
{
	vector<string> cur;
	for (int i = 0; i < ans.size(); ++i)
	{
		string str = "";
		str+=(ans[i]);
		cur.push_back(str);
	}
	for (int i = 0; i < n; i++)
	{
		vector<string> next;
		for (int j = 0; j < cur.size(); j+=2)
		{
			if (cur[j + 1] < cur[j])
			{
				swap(cur[j + 1], cur[j]);
			}
			next.push_back(cur[j] + cur[j + 1]);
		}
		cur = next;
	}
	ans = cur[0];
}

int main(){
#ifdef _CONSOLE 
	freopen("A-large (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		string ans1 = check(n, r, p, s, "S");
		string ans2 = check(n, r, p, s, "P");
		string ans3 = check(n, r, p, s, "R");
		if (ans1 != "")
		{
			ans = ans1;
			mysort(n);
			cout << "Case #" << t << ": "<<ans<<"\n";
			continue;
		}
		if (ans2 != "")
		{
			ans = ans2;
			mysort(n);
			cout << "Case #" << t << ": " << ans<<"\n";
			continue;
		}
		if (ans3 != "")
		{
			ans = ans3;
			mysort(n);
			cout << "Case #" << t << ": " << ans<< "\n";
			continue;
		}
		cout << "Case #" << t << ": IMPOSSIBLE\n";
	}
	

	return 0;
}

