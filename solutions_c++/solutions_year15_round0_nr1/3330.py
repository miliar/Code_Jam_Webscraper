#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<string>
#include<queue>
#include<list>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>
#include<complex>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

int n;

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	cin>>Test;
	for (int T=1;T<=Test;++T)
	{
		printf("Case #%d: ",T);
		string s;
		cin>>n>>s;
		for (int i=0;i<=n;++i)
		{
			int flag=0;
			int t=i;
			for (int j=0;j<=n;++j)
			{
				if (j>t) flag=1;
				t+=s[j]-'0';
			}
			if (!flag)
			{
				printf("%d\n",i);
				break;
			}
		}
	}
	return 0;
}
