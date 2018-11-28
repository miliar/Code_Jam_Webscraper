#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>
using namespace std;


string name;
int n;
int ans;
set<pair<int, int> > s;

bool check(char c)
{
	switch(c)
	{
	case 'a':
	case 'e':
	case 'i':
	case 'o':
	case 'u':
		return false;
		break;
	default:
		return true;
	}
}

void solve()
{
	int count = 0;
	ans = 0;
	int repeat = 0;
	int num = 0;
	int start = 0;
	s.clear();
	for(int i=0; i<name.size(); i++)
	{
		
		if(check(name[i]))
			count++;
		else
			count = 0;
		if(count == 1)
			start = i;
		if(count == n)
		{
			string tmp;
			for(int x=start; x>=0; x--)
			{
				for(int y=i; y<name.size(); y++)
				{
					s.insert(make_pair(x, y));
				}
			}
			i = start;
			count = 0;
		}
	}
	ans = s.size();


}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=0; t<T; t++)
	{
		
		cin>>name>>n;
		solve();
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}

