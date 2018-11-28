#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using std::vector;
using std::string;

char get_winner(char a,char b)
{
	if('R' == a && 'S' == b) return 'R';
	if('R' == a && 'P' == b) return 'P';

	if('S' == a && 'R' == b) return 'R';
	if('S' == a && 'P' == b) return 'S';

	if('P' == a && 'R' == b) return 'P';
	if('P' == a && 'S' == b) return 'S';
}

bool is_success(const string& s)
{
	if(1 == s.size()) return true;
	string result = "";
	for(size_t i = 0;i < s.size();i += 2)
	{
		if(s[i] == s[i+1]) return false;
		result.push_back(get_winner(s[i],s[i+1]));
	}
	return is_success(result);
}

string slove_small(unsigned int n,unsigned int r,unsigned int p,unsigned int s)
{
	unsigned int count = 1<<n;
	vector<char> data(count,'S');
	for(unsigned int i = 0;i < p;++i) data[i] = 'P';
	for(unsigned int i = 0;i < r;++i) data[i+p] = 'R';
	do 
	{
		string s;
		for(unsigned int i = 0;i < count;++i) s.push_back(data[i]);
		if(is_success(s)) return s;
	} while (std::next_permutation(data.begin(),data.end()));
	return "";
}

string slove_quick_help(unsigned int n,unsigned int r,unsigned int p,unsigned int s,const vector<unsigned int>& order)
{
	if(0 == n)
	{
		if(1 == r) return "R";
		else if(1 == p) return "P";
		else return "S";
	}
	unsigned int count = 1<<n;
	if(p > count/2) return "";
	if(s > count/2) return "";
	if(r > count/2) return "";
	vector<unsigned int> no = order;
	no[0] = order[0];no[1] = order[2];no[2] = order[1];
	string ret = slove_quick_help(n-1,count/2 - p,count/2 - s,count/2 - r,no);
	if(0 == ret.size()) return "";
	string ans = "";
	for(size_t i = 0;i < ret.size();++i)
	{
		if('P' == ret[i])
		{
			if(order[0] < order[1]) ans += "PR";
			else ans += "RP";
		}
		else if('R' == ret[i])
		{
			if(order[1] < order[2]) ans += "RS";
			else  ans += "SR";
		}
		else
		{
			if(order[0] < order[2]) ans += "PS";
			else ans += "SP";
		}
	}
	return ans;
}

string nor(const string& s)
{
	size_t len = s.size();
	if(1 == len) return s;
	string s1 = nor(s.substr(0,len/2));
	string s2 = nor(s.substr(len/2));
	if(s1 < s2) return s1 + s2;
	else return s2 + s1;
}

string slove_quick(unsigned int n,unsigned int r,unsigned int p,unsigned int s)
{
	vector<unsigned int> order(3);
	order[0] = 0;order[1] = 1;order[2] = 2;
	string ans = slove_quick_help(n,r,p,s,order);
	if(0 == ans.size()) return ans;
	return nor(ans);
}

int main()
{
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0,r = 0,p = 0,s = 0;scanf("%d%d%d%d",&n,&r,&p,&s);
		//string ans = slove_small(n,r,p,s);
		string ans = slove_quick(n,r,p,s);
		if(0 == ans.size()) printf("Case #%u: IMPOSSIBLE\n",iCases);
		else printf("Case #%d: %s\n",iCases,ans.c_str());
	}
	return 0;
}