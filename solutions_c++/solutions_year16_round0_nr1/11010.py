#include <bits/stdc++.h>
using namespace std;
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define ABS(x) ((x) < 0 ? -1*(x) : (x))
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define INF 2000000000
#define BINF 20000000000000000LL
#define trace(x)                 cerr << #x << ": " << x << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pl;

int counts[10];
int c;

void filldigs(long long int N)
{
	int i;
	while(N)
	{
		i = N % 10;
		if(!counts[i])
			++c;
		++counts[i];
		N /= 10;
	}
}

int main()
{
	fastScan;
	int T,N,i,j;
	cin >> T;

	for(i = 1; i <= T; ++i)
	{
		cin >> N;
		c = 0;
		for(j = 0; j < 10; ++j)
			counts[j] = 0;

		for(j = 1; j <= 1000000 ; ++j)
		{
			filldigs(j*1LL*N);
			if(c == 10)
				break;
		}
		if(c != 10)
			printf("Case #%d: INSOMNIA\n",i);
		else printf("Case #%d: %lld\n",i, j*1LL*N);
	}

	return 0;
}