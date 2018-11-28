#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

bool check(int i)
{
	string s="";
	while(i)
	{
		s += (char)(i%10+48);
		i/=10;
	}
	for(int i=0;i<s.size()/2;i++)
	{
		if(s[i] != s[s.size()-1-i])
			return false;
	}
	return true;
}

bool checkDouble(int x)
{
	double y = sqrt((double)x);
	int z = y;
	if( z == y)
		return true;
	else
		return false;
}

int main()
{
	freopen("C-small-attempt0.in", "rt", stdin); 
	freopen("C-small-attempt0.out", "wt", stdout);
	int t,a,b,ret;
	int x;
	cin >> t;
	int count=1;
	while(t--)
	{
		cin >> a >> b;
		ret=0;
		for(int i=a;i<=b;i++)
		{
			if(checkDouble(i)){
				x = sqrt((double)i);
				if(check(i) && check(x))
					ret++;
			}
		}
		cout << "Case #" << count << ": " << ret << endl;
		count++;
	}
	return 0;
}