#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int T;
long long n,m;
long long gpa(long long k)
{
	string ans="";
	while (k)
	{
		ans+=k%10+'0';
		k/=10;
	}
	string t=ans;
	reverse(t.begin(),t.end());
	ans=t+ans;
	istringstream iss(ans);
	long long tt;
	iss >> tt;
	return tt;
}
long long gpb(long long k)
{
	string ans="";
	while (k)
	{
		ans+=k%10+'0';
		k/=10;
	}
	string t=ans;
	reverse(t.begin(),t.end());
	t.resize(t.size()-1);
	ans=t+ans;
	istringstream iss(ans);
	long long tt;
	iss >> tt;
	return tt;
}
long long ok(long long k,long long ma)
{
	k*=k;
	if (k>ma)
	{
		return 0;
	}
	string ans="";
	while (k)
	{
		ans+=k%10+'0';
		k/=10;
	}
	string t=ans;
	reverse(t.begin(),t.end());

	if (t==ans)
	{
		return 1;
	}
	return 0;
	

}
long long calc(long long num)
{
	long long ans=0;
	for (int i=1;i<=10000;++i)
	{
		if (i>num)
		{
			break;
		}
		long long k=gpa(i);
		
		ans+=ok(k,num);
		k=gpb(i);
		ans+=ok(k,num);
	}
	return ans;
}
int main()
{

	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		cin >> n >> m;
		long long ans=calc(m)-calc(n-1);
		printf("Case #%d: %lld\n",kk,ans);
		
	}


	return 0;

}