#include <iostream>
#include <cstdio>
#include <set>
#define ll long long
using namespace std;
const ll oo = 100000007;
ll n;
set <ll> s;
void phantich(int n)
{
	int nn=n;
	while (nn!=0)
	{
		s.erase(nn%10);
		nn/=10;
	}
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("A-large.in","r",stdin);
	freopen("A.OUT","w",stdout);
	int t;
	cin >> t;
	for (int i=1; i<=t; i++)
	{
		s.clear();
		for (int j=0; j<=9; j++)
			s.insert(j);
		cin >> n;
		ll nn=n;
		while ((s.size()!=0) and (nn!=0))
		{
			phantich(nn);
			nn+=n;
			//cout << "nn = " << nn << '\n';
		}
		nn-=n;
		cout << "Case #" << i << ": ";
		if (s.size()==0) cout << nn;
		else cout << "INSOMNIA";
		if (i!=t) cout << "\n";
	}
	return 0;
}