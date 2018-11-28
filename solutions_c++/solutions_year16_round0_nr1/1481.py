#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define sz(a) ((int)(a).size())
#define mp make_pair
#define fi first
#define se second

typedef pair<int,int> pint;
typedef long long ll;
typedef vector<int> vi;

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		int n;
		scanf("%d",&n);
		if (n==0)
		{
			printf("Case #%d: INSOMNIA\n",asdf);
			continue;
		}
		ll here=n;
		int mask=0;
		do
		{
			for (ll there=here; there; there/=10)
				mask|=1<<(there%10);
			here+=n;
		}
		while (mask!=(1<<10)-1);
		printf("Case #%d: %lld\n",asdf,here-n);
	}
	return 0;
}
