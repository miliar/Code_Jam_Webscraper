#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;
const int INF = -1u>>1;
const double eps = 1e-8;
typedef long long ll;
ll a,b;

bool dp[1111];

bool judge(ll n)
{
	string s;
	while(n)
	{
		int temp = n % 10;
		s.push_back('a'+temp);
		n = n/10;
	}
	int len = s.length();
	bool flag = true;
	for(int i=0;i<len/2;++i)
	{
		if(s[i] != s[len-i-1])
		{
			flag = false;
			break;
		}
	}
	return flag;
}
void init()
{
	memset(dp,false,sizeof(dp));
	for(int i=1;i<=33;i++)
	{
		if(judge(i) && judge(i*i))
		{
			dp[i*i] = true;
		}
	}
}

int main()
{
	init();
	ifstream in;
	ofstream out;
	in.open("D:\\C-small-attempt0.in");
	out.open("D:\\c.out");
	int T;
	in>>T;
	for(int cas=1;cas<=T;cas++)
	{
		in>>a>>b;
		int ans = 0;
		for(int i=a;i<=b;++i)
		{
			if(dp[i]) ans++;
		}
		//printf("Case #%d: %d\n",cas,ans);
		out<<"Case #"<<cas<<": "<<ans<<endl;
	}
  return 0;
}

