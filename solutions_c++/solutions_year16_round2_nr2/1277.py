// close match

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

vector<string> v1, v2;
string s1, s2;
int sz1, sz2;

void init()
{
	v1.clear();
	v2.clear();
	s1 = "";
	s2 = "";
	sz1 = 0;
	sz2 = 0;
	return;
}


void dfs(string k, int idx, int sz, int type)
{
	if(idx == sz)
	{
		if(type == 1)v1.push_back(k);
		if(type == 2)v2.push_back(k);
		return;
	}
	if(k[idx] != '?')
	{
		dfs(k, idx + 1, sz, type);
		return;
	}
	for(int i = 0; i < 10; ++i)
	{
		k[idx] = ('0' + i);
		dfs(k, idx + 1, sz, type);
	}
}

int num(string p)
{
	int r = 0;
	for(int i = 0; i < (int)p.size(); ++i)
	{
		r = 10 * r + (p[i] - '0');
	}
	return r;
}

int abs_diff(int k)
{
	if(k < 0)return -1 * k;
	return k;
}

int main()
{
	
	int tc, cs = 1;
	cin >> tc;
	while(tc--)
	{
		init();
		cin >> s1 >> s2;
		
		sz1 = (int)s1.size();
		sz2 = (int)s2.size();
	
	    dfs(s1, 0, sz1, 1);	
	    dfs(s2, 0, sz2, 2);
	    
	    int z1 = (int)v1.size();
	    int z2 = (int)v2.size();
	    
	    string a1, a2;
	    //cout << z1 << " " << z2 << endl;
	    
		int mn_diff = 9999999;
	    
	    for(int i = 0; i < z1; ++i)
	    for(int j = 0; j < z2; ++j)
	    {
	    	int n1 = num(v1[i]);
	    	int n2 = num(v2[j]);
	    	if(abs_diff(n1 - n2) < mn_diff)
	    	{
	    		mn_diff = abs_diff(n1 - n2);
	    		a1 = v1[i];
	    		a2 = v2[j];
			}
			if(abs_diff(n1 - n2) == mn_diff)
			{
				if(num(v1[i]) < num(a1))
				{
					a1 = v1[i];
				}
				if(num(v2[j]) < num(a2))
				{
					a2 = v2[j];
				}
			}
		}
		printf("Case #%d: ", cs++);
		cout << a1 << " " << a2 << endl;
	    
	}
	return 0;
}
