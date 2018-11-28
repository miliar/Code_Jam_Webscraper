#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>  
using namespace std;  

#define PB push_back  
#define MP make_pair  

#define REP(i,n) for(i=0;i<(n);++i)  
#define FOR(i,l,h) for(i=(l);i<=(h);++i)  
#define FORD(i,h,l) for(i=(h);i>=(l);--i)  
#define CLOCK cout << "Clock " << (double)clock()/CLOCKS_PER_SEC << endl
const int maxs = 103;

long long toNum(string str)
{
	long long res= 0ll;
	for (int i=0;i<str.length();i++)
		res = res*10 + (str[i]-'0');
	return res;
}
pair<long,long> getNum(long long num)
{
	long long tmp = num;
	string str = "",tstr="";
	while(tmp)
	{
		str += tmp%10 +'0';
		tmp /= 10;
	}
	tstr = str;
	reverse(str.begin(),str.end());
	string str1 = str + tstr;
	string str2 = str + tstr.substr(1);
	long long num1 = toNum(str1) * toNum(str1);
	long long num2 = toNum(str2) * toNum(str2);
	return std::make_pair(num1,num2);
}

bool isPalin(long long num)
{
	string str = "";
	while (num)
	{
		str += num%10 + '0';
		num/=10;
	}
	for (int i=0;i<str.length()/2;i++)
	{
		if (str[i] != str[str.length()-1-i])
			return false;
	}
	return true;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	long long n,m;
	for(int cases=1;cases<=t;cases++)
	{
		cin >> n >> m;
		long long res = 0;
		for (long long i=1;i<=10000;i++)
		{
			pair<long long,long long> num = getNum(i);
			if (num.first>=n && num.first<=m && isPalin(num.first))
			{
				res ++;
			}
			if (num.second>=n && num.second<=m && isPalin(num.second))
			{
				res ++;
			}
		}
		printf("Case #%d: ",cases);
		cout << res << endl;
	}
	return 0;
}