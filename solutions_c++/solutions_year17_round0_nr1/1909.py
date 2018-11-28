#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define RFOR(i,b,a) for (int i = (b)-1; i >= (a); --i)
#define ITER(it,a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define FILL(a,value) memset(a, value, sizeof(a))

#define SZ(a) (int)a.size()
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double PI = acos(-1.0);
const int INF = 1000 * 1000 * 1000 + 7;
const LL LINF = 1LL * INF * INF;

const int MAX = 1010;
bool A[MAX];

void turn(int l,int r)
{
	FOR(i,l,r+1)A[i]^=1;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	FOR(tt,0,t)
	{
		string s;
		cin>>s;
		int n =SZ(s);
		int k;
		cin>>k;

		FOR(i,0,n)
		{
			A[i]=s[i]=='+';
		}

		bool ok = true;
		int ans = 0;
		FOR(i,0,n)
		{
			if(A[i]==0)
			{
				int r = i+k-1;
				if(r>=n)
				{
					ok = false;
					break;
				}
				turn(i,r);
				++ans;
			}
		}

		cout<<"Case #"<<tt+1<<": ";
		if(!ok)
		{
			cout<<"IMPOSSIBLE\n";
		}else
		{
			cout<<ans<<"\n";
		}
	}
}
