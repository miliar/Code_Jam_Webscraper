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
char get(char a, bool b)
{
	if (b)
		return toupper(a);
	return a;
}
char mul(char a, char b)
{
	bool am = isupper(a);
	bool bm = isupper(b);
	a = tolower(a);
	b = tolower(b);

	if (a=='e')
		return get(b,bm!=am);
	if (b=='e')
		return get(a,bm!=am);
	if (a=='i')
	{
		if (b=='i')
			return get('e',!(bm!=am));
		if (b=='j')
			return get('k',(bm!=am));
		if (b=='k')
			return get('j',!(bm!=am));
	}
	if (a=='j')
	{
		if (b=='i')
			return get('k',!(bm!=am));
		if (b=='j')
			return get('e',!(bm!=am));
		if (b=='k')
			return get('i',(bm!=am));
	}
	if (a=='k')
	{
		if (b=='i')
			return get('j',(bm!=am));
		if (b=='j')
			return get('i',!(bm!=am));
		if (b=='k')
			return get('e',!(bm!=am));
	}
}
void go()
{	
	int l,x;
	cin>>l>>x;
	string sum;
	string temp;
	cin>>temp;
	for (int i=0;i<x;i++)
		sum+=temp;
	if (sum.size()<3)
	{
		cout<<"NO";
		return ;
	}
	vector<char> to(sum.size());
	vector<char> from(sum.size());
	char src = 'e';
	for (int i=0;i<sum.size();i++)
	{
		to[i]=mul(src,sum[i]);
		src = to[i];
	}
	src = 'e';
	for (int i=sum.size()-1;i>=0;i--)
	{
		from[i]=mul(sum[i], src);
		src = from[i];
	}
	for (int i=0;i<sum.size()-2;i++)
	{
		char cur = to[i];
		if (cur!='i')
			continue;
		char curs = 'e';
		for (int j=i+1;j<sum.size()-1;j++)
		{
			curs = mul(curs, sum[j]);
			if (curs=='j' && from[j+1]=='k')
			{
				cout<<"YES";
				return ;
			}
		}
	}
	cout<<"NO";
}
int main()
{	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("2.out","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		if (curcase!=cases)
			cout<<"\n";
	}
	return 0;
}
