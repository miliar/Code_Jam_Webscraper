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
int solve()
{
	long long a, n;
	cin>>a>>n;
	vector<int> motes(n);
	for(int i=0; i<n; i++)
	{
		cin>>motes[i];
	}
	sort(motes.begin(), motes.end());
	int ans=n;
	int c=0;
	for(int i=0; i<n; i++)
	{
		int ca;
		if(motes[i]<a)
		{
			ca=c+n-i-1;
			a+=motes[i];
		}
		else
		{
			if(a==1)
				return ans;
			while(!(motes[i]<a))
			{
				c++;
				a+=a-1;
			}
			ca=c+n-i-1;
			a+=motes[i];
		}
		ans=min(ans, ca);
	}
	return ans;
}
int main() {
	ios_base::sync_with_stdio(false);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int i=0; i<t; i++)
	{
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
}
