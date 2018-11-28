#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;

int dfs(string s, int cur, char cmp,int ans)
{
	if (cur == -1)return ans;
	if (s[cur] == cmp) return dfs(s, cur - 1, cmp, ans);
	else return dfs(s, cur - 1, s[cur], ans + 1);
}
int main()
{
	int n;
	ifstream ifs;
	ofstream ofs;

	ifs.open("input.txt");
	ofs.open("output.txt");

	ifs >> n;
	for (int ca = 1; ca <= n; ca++)
	{
		string s;
		
		ifs >> s;
		int len = s.length() - 1;
		ofs << "Case #"<<ca<<": "<<dfs(s, len, '+', 0)<<"\n";
	}
}