#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <ctime>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;

struct val
{
	char ch;
	int sgn;
};

val s[10010],pro;
ll cases,l,x,r1,r2,ind1,ind2,cnt;
bool flag;

val mul(val a,val b)
{
	val res;
	if(a.sgn == b.sgn)
	{
		res.sgn=0;
	}
	else
	{
		res.sgn=1;
	}
	if(a.ch=='1')
	{
		res.ch=b.ch;
	}
	else if(a.ch=='i')
	{
		if(b.ch=='1')
		{
			res.ch='i';
		}
		else if(b.ch=='i')
		{
			res.ch='1';
			res.sgn=1-res.sgn;
		}
		else if(b.ch=='j')
		{
			res.ch='k';
		}
		else if(b.ch=='k')
		{
			res.ch='j';
			res.sgn=1-res.sgn;
		}
	}
	else if(a.ch=='j')
	{
		if(b.ch=='1')
		{
			res.ch='j';
		}
		else if(b.ch=='i')
		{
			res.ch='k';
			res.sgn=1-res.sgn;
		}
		else if(b.ch=='j')
		{
			res.ch='1';
			res.sgn=1-res.sgn;
		}
		else if(b.ch=='k')
		{
			res.ch='i';
		}
	}
	else if(a.ch=='k')
	{
		if(b.ch=='1')
		{
			res.ch='k';
		}
		else if(b.ch=='i')
		{
			res.ch='j';
		}
		else if(b.ch=='j')
		{
			res.ch='i';
			res.sgn=1-res.sgn;
		}
		else if(b.ch=='k')
		{
			res.ch='1';
			res.sgn=1-res.sgn;
		}
	}
	return res;
}

int main()
{
	std::ios::sync_with_stdio(false);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	cin>>cases;
	for(ll kase=1;kase<=cases;kase++)
	{
		cin>>l>>x;
		for(ll i=0;i<l;i++)
		{
			cin>>s[i].ch;
			s[i].sgn=0;
		}
		cout<<"Case #"<<kase<<": ";
		flag=false;
		pro.ch='1';
		pro.sgn=0;
		for(ll i=1;i<=4;i++)
		{
			for(ll j=0;j<l;j++)
			{
				pro=mul(pro,s[j]);
				if(pro.ch=='i' && pro.sgn==0)
				{
					flag=true;
					ind1=j;
					r1=i;
					break;
				}
			}
			if(i==x || flag)break;
		}
		if(!flag)
		{
			cout<<"NO\n";
			continue;
		}
		pro.ch='1';
		pro.sgn=0;
		flag=false;
		for(ll i=1;i<=4;i++)
		{
			for(ll j=l-1;j>=0;j--)
			{
				pro=mul(s[j],pro);
				if(pro.ch=='k' && pro.sgn==0)
				{
					flag=true;
					ind2=j;
					r2=x-i+1;
					break;
				}
			}
			if(i==x || flag)break;
		}
		if(!flag)
		{
			cout<<"NO\n";
			continue;
		}
		if(r1==r2)
		{
			pro.ch='1';
			pro.sgn=0;
			for(ll i=ind1+1;i<ind2;i++)
			{
				pro=mul(pro,s[i]);
			}
			if(pro.ch=='j' && pro.sgn==0)
			{
				cout<<"YES\n";
			}
			else
			{
				cout<<"NO\n";
			}
		}
		else if(r1<r2)
		{
			cnt=(r2-r1-1)%4;
			pro.ch='1';
			pro.sgn=0;
			for(ll i=ind1+1;i<l;i++)
			{
				pro=mul(pro,s[i]);
			}
			for(ll i=1;i<=cnt;i++)
			{
				for(ll j=0;j<l;j++)
				{
					pro=mul(pro,s[j]);
				}
			}
			for(ll i=0;i<ind2;i++)
			{
				pro=mul(pro,s[i]);
			}
			if(pro.ch=='j' && pro.sgn==0)
			{
				cout<<"YES\n";
			}
			else
			{
				cout<<"NO\n";
			}
		}
		else
		{
			cout<<"NO\n";
		}
	}
	return 0;
}