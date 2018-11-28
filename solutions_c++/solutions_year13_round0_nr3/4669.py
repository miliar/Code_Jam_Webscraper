#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include<fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;

#define oo 100000000000000
#define oom 10000005
vector <long long> v;

bool fair (long long i)
{
	string s="";
	while (i != 0)
	{
		s+= ((i%10)+48);
		i /= 10;
	}
	for (int j=0; j<s.size(); j++)
	{
		if (s[j] != s[s.size()-1-j])
			return false;
	}
	return true;
}
bool arr[oom];
void fairAndSquare ()
{
	memset(arr,false,sizeof(arr));
	for (int i=1; i<oom; i++)
	{
		arr[i] = fair(i);
	}
	for (long long i=1; i*i<=oo; i++)
	{
		if (i*i < oom)
		{
			if (arr[i] && arr[i*i])
			{
				v.push_back(i*i);
			}
		}
		else
		{
			if (arr[i] && fair(i*i))
			{
				v.push_back(i*i);
			}
		}
	}
}

int main ()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);

	fairAndSquare();

	/*long long arra[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
	v = vector < long long > (arra,arra+39);*/

	long long T,n,m;
	scanf("%lld",&T);
	for (int t=1; t<=T; t++)
	{
		scanf("%lld %lld",&n,&m);
		int count = 0;
		for (int i=0; i<v.size(); i++)
		{
			if (n <= v[i] && v[i] <= m)
			{
				count++;
			}
		}
		
		printf("Case #%d: %d\n",t,count);
	}


	return 0;
}