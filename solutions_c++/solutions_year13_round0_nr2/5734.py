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

/*
	
	2 0 2
	1 0 1
	2 0 2
	"YES"

	2 2 2 2 2
	2 1 1 1 2
	2 1 2 1 2
	2 1 1 1 2
	2 2 2 2 2
	"NO"

	1 2 1
	"YES"
	*/

bool checkCell(int row, int col, vector<vector<int> >v)
{
	bool r,c;
	r=c=false;
	for(int i=0;i<v.size();i++)
	{
		if(v[row][col] < v[i][col])
			r=true;
	}
	for(int i=0;i<v[0].size();i++)
	{
		if(v[row][col] < v[row][i])
			c=true;
	}
	if(r&&c)
		return true;
	else
		return false;
}

bool check(vector<vector<int> >v)
{
	for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<v[i].size();j++)
		{
			if(checkCell(i,j,v)) // true lw feh moshkla.
			{
				return false;
			}
		}
	}
	return true;
}

int main () 
{
	freopen("B-small-attempt0.in", "rt", stdin); 
	freopen("B-small-attempt0.out", "wt", stdout);
	int t,n,m,x,c=1,max;
	cin >> t;
	while(t--)
	{
		cin >> n >> m;
		vector<vector<int> >v(n);
		max=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin >> x;
				if(x > max)
					max = x;
				v[i].push_back(x);
			}
		}
		cout << "Case #" << c++ << ": " ;
		if(check(v))
		{
			cout << "YES";
		}
		else
		{
			cout << "NO";
		}
		cout << endl;
	}
	return 0;
}





	/*#include <vector>
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

	bool check(long long i)
	{
	string s="";
	while(i)
	{
	s += (char)(i%10+48);
	i/=10;
	}
	for(long long i=0;i<s.size()/2;i++)
	{
	if(s[i] != s[s.size()-1-i])
	return false;
	}
	return true;
	}

	bool checkDouble(long long x)
	{
	long double y = sqrt((long double)x);
	long long z = y;
	if( z == y)
	return true;
	else
	return false;
	}

	int main()
	{
	freopen("C-large-1.in", "rt", stdin); 
	freopen("C-large-1.out", "wt", stdout);
	int t;
	long long a,b,ret,x,count=1;
	cin >> t;
	while(t--)
	{
	cin >> a >> b;
	ret=0;
	for(long long i=a;i<=b;i++)
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
	}*/