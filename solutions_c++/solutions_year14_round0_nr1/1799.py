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
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int T;
	cin>>T;
	for (int TT=1;TT<=T;++TT)
	{
		printf("Case #%d: ",TT);
		int r;
		int a[6][6];
		cin>>r;
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				cin>>a[i][j];
		set<int> H;
		for (int j=1;j<=4;++j)
			H.insert(a[r][j]);
		cin>>r;
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				cin>>a[i][j];
		vector<int> v;
		for (int j=1;j<=4;++j)
			if (H.count(a[r][j])) v.push_back(a[r][j]);
		if (v.size()==1)
			cout<<v[0]<<endl;
		else if (v.empty())
			puts("Volunteer cheated!");
		else
			puts("Bad magician!");
	}
	return 0;
}
