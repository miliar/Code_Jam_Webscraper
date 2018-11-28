#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;

void go()
{	
	int n;
	cin>>n;
	string s;
	cin>>s;
	int res = 0;
	int sum = 0;
	for (int i=0;i<s.size();i++)
	{
		if (s[i]!='0' && sum>=i)
		{
			sum+=s[i]-'0';
		}
		else if (s[i]!='0')
		{
			res+=i-sum;
			sum+=i-sum+s[i]-'0';
		}
	}
	cout<< res;
}
int main()
{	
	freopen("A-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		cout<<"\n";
	}
	return 0;
}
