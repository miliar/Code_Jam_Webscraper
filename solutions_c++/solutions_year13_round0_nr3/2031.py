#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;
const int base = 10;
typedef vector<int> lnum;
bool lq(const lnum& a,const lnum& b)
{
	if (a.size()!=b.size())
		return a.size()<=b.size();
	for (int i=a.size()-1;i>=0;i--)
		if (a[i]!=b[i])
			return a[i]<=b[i];
	return true;
}
lnum mul(const lnum& a,const lnum& b)
{
	lnum res;
	for (int i=0;i<a.size();i++)
	{
		int carry =0;
		for (int j=0;j<b.size()||carry;j++)
		{
			if (i+j>=res.size())
				res.push_back(0);
			carry+=res[i+j]+a[i]*(j<b.size()? b[j] :0);
			res[i+j]= carry%10;
			carry/=10;
		}
	}
	while (res.size() &&  res.back() ==0)
		res.pop_back();
	return res;
}
lnum current;
lnum upper;
bool stop(bool even)
{
	lnum tmp = current;
	for (int i=current.size()-1-even;i>=0;i--)
		tmp.push_back(current[i]);

	if (lq(mul(tmp,tmp),upper))
		return 0;
	return 1;
}
int cursum;
long long res;
void rec()
{
	for (int i=0;i<10;i++)
	{
		if (i==0 && cursum ==0)
			continue;
		if (2*i*i+cursum<10)
		{
			current.push_back(i);
			cursum+=2*i*i;
			if (!stop(false))
			{
				res++;
				rec();
			}
			cursum-=2*i*i;
			current.pop_back();
		}
		if (i*i+cursum<10)
		{
			current.push_back(i);
			cursum+=i*i;
			if (!stop(true))
			{
				res++;
			}
			cursum-=i*i;
			current.pop_back();
		}
		else
			return;
	}
}
void dec(lnum &a)
{
	for (int i=0;i<a.size();i++)
	{
		a[i]--;
		if (a[i]==-1)
			a[i]+=10;
		else
			break;
	}
	while (a.size() &&  a.back() ==0)
		a.pop_back();
	return ;
}


int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int testcount;
	cin>>testcount;
	for (int curtest =1;curtest<=testcount;curtest++)
	{
		lnum a,b;
		string tmp;
		cin>>tmp;
		for (int i=tmp.size()-1;i>=0;i--)
		{
			a.push_back(tmp[i]-'0');
		}
		cin>>tmp;
		for (int i=tmp.size()-1;i>=0;i--)
		{
			b.push_back(tmp[i]-'0');
		}
		cursum=0;
		res=0;
		current.resize(0);
		upper = b;
		rec();
		long long result = res;
		cursum=0;
		res=0;
		current.resize(0);
		upper = a;
		dec(upper);
		rec();
		result-=res;
		cout<<"Case #"<<curtest<<": "<<result<<"\n";
	}
	

	return 0;
}