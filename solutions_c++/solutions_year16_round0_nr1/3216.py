#include <bits/stdc++.h>
using namespace std;
#define all(c) (c).begin(), (c).end()
#define cnt(c, x) ((c).find(x) != (c).end())
#define pb push_back
#define FOR(i, a, n) for(int i = (a); i < (n); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int) (x).size())
#define mp(x,y) make_pair((x), (y))
#define mp3(x,y,z) make_pair((x), make_pair( (y), (z)))
#define foreach(C, i) for(auto i = (C).begin(); i != (C).end(); i++)
#define xx first
#define yy second
#define clr clear()
#define var(x) cout<< #x << " = "<<x<<"\n";
#define print(x) for_each((x).begin(), (x).end(), [](auto n) { cout<<x<<" " })
typedef int32_t i3;
typedef int64_t i6;
typedef vector<i3> vi;
typedef pair<i3,i3> ii;
typedef vector<pair<i3,i3> > vii;

bool isGood(vector<int>& mp)
{
	for(int i = 0; i < 10; i++)
	{
		if (mp[i] == 0 )
			return false;
	}
	return true;
}

i6 getIter(i6 num)
{
	i6 cnt = 1;	
	vector<int> mps(10,0);
	while (!isGood(mps))
	{
		i6 newNum = cnt*num;
		cnt++;
		while (newNum)
		{
			int d = newNum%10;
			mps[d]++;
			newNum /= 10;
		}
	}
	return (cnt-1)*num;
}

int main()
{
	ios::sync_with_stdio(false);
	i6 tc; cin>>tc;
	FOR(i,1,tc+1)
	{
		cout<<"Case #"<<i<<": ";
		i6 num; cin>>num;
		if (num == 0)
			cout<<"INSOMNIA\n";
		else
		{
			i6 ans = getIter(num);
			cout<<ans<<"\n";
		}
	}
	return (0);
}
