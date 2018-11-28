#include <iostream>
#include <string>
#include <map>
using namespace std;
map<pair<string, string>, string> mul;
string target[] = { "i", "j", "k" };
int dp[3][10001];
string multiply(string& s1, string& s2)
{
	if (s1.empty())
	{
		if (s2.empty()) {
			return "";
		}
		return s2;
	}
	if (s2.empty()) {
		return s1;
	}
	int sgn=1;
	if (s1[0] == '-')
	{
		sgn *= -1;
		s1 = s1.substr(1);
	}
	if (s2[0] == '-')
	{
		sgn *= -1;
		s2 = s2.substr(1);
	}
	string res = mul[pair<string, string>(s1, s2)];
	if (sgn == -1)
	{
		if (res[0] == '-')
			return res.substr(1);
		else
			return "-" + res;
	}
	return res;
}
bool Perm(string& str, int pos = 0, int t = 0)
{
	if (pos >= str.size())
	{
		return t == 3;
	}
	if (dp[t][pos] != -1)
		return dp[t][pos];
	if (t == 2)
	{
		string res;
		for (int i = pos; i < str.size(); i++)
		{
			string g;
			g = str[i];
			res = multiply(res, g);
		}
		dp[t][pos] = (res == target[t]) ? 1 : 0;
		return res == target[t];
	}
	else
	{
		string res;
		for (int i = pos; i < str.size(); i++)
		{
			string g;
			g = str[i];
			res = multiply(res, g);
			if (res == target[t])
			{
				bool f = Perm(str, i + 1, t + 1);
				if (f)
				{
					dp[t][i] = true;
					return true;
				}
				else
				{
					dp[t][i] = false;
				}
			}
		}
	}
	dp[t][pos] = false;
	return false;
}
int main()
{
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("1", "1"), "1"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("1", "i"), "i"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("1", "j"), "j"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("1", "k"), "k"));

	mul.insert(pair<pair<string, string>, string>(pair<string, string>("i", "1"), "i"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("i", "i"), "-1"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("i", "j"), "k"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("i", "k"), "-j"));

	mul.insert(pair<pair<string, string>, string>(pair<string, string>("j", "1"), "j"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("j", "i"), "-k"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("j", "j"), "-1"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("j", "k"), "i"));

	mul.insert(pair<pair<string, string>, string>(pair<string, string>("k", "1"), "k"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("k", "i"), "j"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("k", "j"), "-i"));
	mul.insert(pair<pair<string, string>, string>(pair<string, string>("k", "k"), "-1"));

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		for (int i = 0; i < 3; i++)
			for (int j = 0; j < 10001; j++)
				dp[i][j] = -1;
		string str = "";
		int L, X;
		cin >> L >> X;
		cin.get();
		string temp;
		getline(cin, temp, '\n');
		for (int i = 0; i < X; i++)
		{
			str = str + temp;
		}
		bool flag = Perm(str);
		cout << "Case #" << t << ": " << ((flag) ? "YES" : "NO") << endl;
	}
	return 0;
}