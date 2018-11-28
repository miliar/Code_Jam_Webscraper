#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<functional>
#include<algorithm>

using namespace std;

//#define _INFILE		"A.in"
//#define _OUTFILE	"A.out"

//#define _INFILE		"A-small-attempt5.in"
//#define _OUTFILE	"A-small.out"

#define _INFILE		"A-large.in"
#define _OUTFILE	"A-large.out"
int best[128];
	
void solve()
{
	int a, n;
	scanf("%d%d",&a,&n);

	vector<int> v;
	v.reserve(128);

	for(int i=0; i<n; i++)
		best[i] = -1;

	for(int i=0; i<n; i++)
	{
		int t;
		scanf("%d",&t);
		v.push_back(t);
	}

	sort(v.begin(), v.end());
	int result = 0;
	for(int i=0; i<v.size(); i++)
	{
		best[i] = result + v.size() - i;
		if (a<=v[i])
		{
			int k = 0;
			int b = a;
			while(a > 1 && b <= v[i])
			{
				k++;
				b += b - 1;
			}
			if ( b > v[i] )
			{
				result += k;
				a = b;
			}
			else
			{
				result = best[i];
				break;
			}
		}
		a += v[i];
	}

	for(int i=0; i<n; i++)
	{
		if (best[i] >= 0 && result > best[i])
		{
			result = best[i];
		}
	}

	printf("%d\n",result);
}

int main(void)
{
	int T;
	freopen(_INFILE, "r", stdin);
	freopen(_OUTFILE, "w", stdout);

	scanf("%d",&T);

	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

