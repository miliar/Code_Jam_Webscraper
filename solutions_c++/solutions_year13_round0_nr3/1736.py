#include <cstdio>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm> 

using namespace std;

#define forn(x,y) for(int x=0;x<y;x++)
#define mp make_pair 
#define pb push_back
#define inf 0x7f7f7f7f

typedef long long i64;

vector <int> t1,t2;
bool p(i64 x)
{
 	t1.clear();
 	t2.clear();
	int y;
	while(x>0)
	{
		y=x%10;
		x/=10;
		t1.pb(y);
		t2.pb(y);
	}
	reverse(t1.begin(),t1.end());
	forn(i,t2.size())
		if (t1[i]!=t2[i])
			return 0;
		return 1;
}

int test,tests;
vector <i64> precalc;
int ans;
i64 l,r;

int main()
{
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);

	cin >> tests;
	for (i64 i=1;i*i<100000000000000;i++)
	{
		if(p(i))
			if(p(i*i))
				precalc.pb(i*i);
	}
	/*cerr << "size:" << precalc.size();
	forn(i,precalc.size())
		cerr << precalc[i] << " ";*/
	forn(test,tests)
	{
		//scanf("%I64d%I64d\n",&l,&r);
		cin >> l >> r;
		ans=0;

	 	forn(i,precalc.size())
	 	{
	 		if(precalc[i]>=l && precalc[i]<=r)
	 			ans++;
	 	}
	 	printf("Case #%d: %d\n",test+1,ans);
	}
	return 0;
}
