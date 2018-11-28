#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<iostream>
#include<map>


using namespace std;

#define rep(i,n) for(int i=0; i<(int)n; i++)
#define st first
#define nd second
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpii;
typedef set<int> SI;
typedef long long LL;

#ifdef DEBUG
const bool debug = true;
#else
const bool debug = false;
#endif
int n,m,k,l, t = 1;
const int inf = 1000 * 1000 * 1000 ;
const LL MAKSN = 1000 * 1000 + 13; // UZUPElnic
LL N;

bool czy[11] = {false};

void readIn()
{
	cin >> N;
}

void addNumber(long long a) 
{
	if (a == 0)
	{
		czy[0] = true;
		return;
	}

  	while(a != 0)
  	{
  		czy[a%10] = true;
  		a /= 10;
  	}
}

bool wereAll()
{
	rep(i, 10)
	if (!czy[i])
		return false;
	return true;
}

void solve()
{
	rep(i, MAKSN)
	{
		LL cur = N * (i+1);
		addNumber(cur);
		if(wereAll())
		{
			cout << cur << "\n";
			return;
		}
	}

	cout << "INSOMNIA\n";
}

void zeruj()
{
	rep(i, 10)
	czy[i] = false;
}

int main()
{
	cin >> t;

	rep(i, t)
	{
		cout << "Case #" << i + 1 << ": ";
		zeruj();
		readIn();
		solve();
	}

	return 0;
}
