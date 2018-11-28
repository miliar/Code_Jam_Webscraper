#include<fstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<iostream>
#include<map>
using namespace std;

map< pair<char, char>, char> symb_map;

void fill_map()
{
	symb_map[make_pair('1','i')] = 'i';
	symb_map[make_pair('1','j')] = 'j';
	symb_map[make_pair('1','k')] = 'k';
	symb_map[make_pair('i','1')] = 'i';
	symb_map[make_pair('j','1')] = 'j';
	symb_map[make_pair('k','1')] = 'k';
	symb_map[make_pair('i','j')] = 'k';
	symb_map[make_pair('j','k')] = 'i';
	symb_map[make_pair('k','i')] = 'j';
}

const int nmax = 10000;
bool prepi[nmax + 1];
bool prepk[nmax + 1];

bool solve(const string& s)
{
	for(int i = 0;i <= nmax;++i)
	{
		prepi[i] = false;
		prepk[i] = false;
	}
	
	int sz = s.size();
	
	//Preprocess for i
	
	char prev = '1';
	bool minus = false;
	for(int i = 0;i < sz;++i)
	{
		if(symb_map.find(make_pair(prev, s[i])) == symb_map.end())
		{
			if(prev == s[i])
			{
				prev = '1';
			}
			else
			{
				prev = symb_map[make_pair(s[i], prev)];
			}
			minus = !minus;
		}
		else
		{
			prev = symb_map[make_pair(prev, s[i])];
		}
		
		if(prev == 'i' && minus == false)
		{
			prepi[i] = true;
		}
	}
	
	//Preprocess for k
	
	prev = '1';
	minus = false;
	
	for(int i = sz - 1;i >=0;--i)
	{
		if(symb_map.find(make_pair(s[i], prev)) == symb_map.end())
		{
			if(s[i] == prev)
			{
				prev = '1';
			}
			else
			{
				prev = symb_map[make_pair(prev, s[i])];
			}
			minus = !minus;
		}
		else
		{
			prev = symb_map[make_pair(s[i], prev)];
		}
		
		if(prev == 'k' && minus == false)
		{
			prepk[i] = true;
		}
	}
	
	//Preprocess for j
	
	int pozj = -1;
	map<char, int> mp;
	mp['1'] = 0;
	mp['i'] = 1;
	mp['j'] = 2;
	mp['k'] = 3;
	
	prev = '1';
	minus = false;
	for(int i = 0;i < sz - 1;++i)
	{
		if(symb_map.find(make_pair(prev, s[i])) == symb_map.end())
		{
			if(prev == s[i])
			{
				prev = '1';
			}
			else
			{
				prev = symb_map[make_pair(s[i], prev)];
			}
			minus = !minus;
		}
		else
		{
			prev = symb_map[make_pair(prev, s[i])];
		}
		
		if(prepk[i + 1] == true && minus == false && prev == 'k')
		{
			pozj = i;
		}
	}
	
	/* Do the final step */
	
	for(int i = 0;i < sz - 2;++i)
	{
		if(prepi[i] == true && pozj > i)
		{
			return true;
		}
	}
	
	return false;
}

int main()
{
	ifstream in("C.in");
	ofstream out("C.out");
	
	fill_map();
	string s;
	
	int t;
	
	getline(in, s);
	t = atoi(s.c_str());
	
	for(int i = 0;i < t;++i)
	{
		getline(in, s);
		
		int j = 0;
		while(s[j] != ' ')
		{
			++j;
		}
		++j;
		
		string s1;
		for(;j < (int) s.size();++j)
		{
			s1 += s[j];
		}
		
		int x;
		
		x = atoi(s1.c_str());
		getline(in, s);
		
		string prob;
		for(int j = 0;j < x;++j)
		{
			prob += s;
		}
		
		bool ans = solve(prob);
		
		if(ans)
		{
			out<<"Case #"<<i + 1<<": "<<"YES\n";
		}
		else
		{
			out<<"Case #"<<i + 1<<": "<<"NO\n";
		}
	}
	
	in.close();
	out.close();
}
