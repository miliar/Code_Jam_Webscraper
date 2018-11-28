#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector <long long> v;

bool ispal(string str)
{
	string cp = str;
	reverse (cp.begin(),cp.end());
	if (cp == str)
		return true;
	return false;
}

string tostr (long long n)
{
	string ret = "";
	while (n)
	{
		ret += n%10+'0';
		n/=10;
	}
	return ret;
}

long long tolong (string str)
{
	long long ret = 0;
	int i;
	for (i=0;i<str.size();i++)
	{
		ret*=10LL;
		ret+=(long long)(str[i]-'0');
	}
	return ret;
}

string dupl(string s,int n)
{
	string ret;
	if (n == s.size()*2)
	{
		ret = s;
		reverse (ret.begin(),ret.end());
	}
	else
	{
		ret = s.substr(0,s.size()-1);
		reverse (ret.begin(),ret.end());
	}
	return s+ret;
}

void sol (int ind,string cur)
{
	if (ind == 4)
		return;
	if (ind)
	{
		long long c = tolong (dupl(cur,2*cur.size()));
		long long s = c*c;
		if (ispal(tostr(s)))
			v.push_back(s);
		//cout << cur << " " << c << " " << s << endl;
		c = tolong (dupl(cur,2*cur.size()-1));
		s = c*c;
		//cout << cur << " " << c << " " << s << endl;
		if (ispal(tostr(s)))
			v.push_back(s);
		
	}
	for (int i=ind?0:1;i<10;i++)
		sol (ind+1,cur+(char)(i+'0'));
	return ;
}

int main()
{
	sol (0,"");/*
	printf ("%d\n",v.size());
	for (int i=0;i<v.size();i++)
		printf ("%lld %llf\n",v[i],sqrt(v[i]));*/
	
	freopen ("C.in","r",stdin);
	freopen ("C.out","w",stdout);
	
	int t,o=1;
	scanf ("%d",&t);

	while (t--)
	{
		long long a,b;
		int i;
		scanf ("%lld %lld",&a,&b);

		int ret = 0;
		for (i=0;i<v.size();i++)
			if (v[i]<=b&&v[i]>=a)
				ret++;
		printf ("Case #%d: %d\n",o++,ret);

	}
	
	return 0;
}
