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
const int MAKSN = 1000 * 1000 + 13; // UZUPElnic
string s;

vi res;

void readIn()
{
	cin >> n >> k;
}

LL divisor(LL num)
{
	for(LL i = 2; i * i <= num; i++)
		if(num % i == 0) 
			return i;
	return 0;
}

LL checkSys(LL num, int sys)
{
	LL res = 0;
	LL cur = 1;
	rep(i, 32)
	{
		if(num & (1 << i))
		{
			res += cur;
		}
		cur *= sys; 
	}
	// cout << "sys = " <<sys << "-> " << res <<"\n";

	return (divisor(res));
}

void writeOut(LL nr)
{
	for(int i = n - 1; i >= 0; i--)
		if(nr & (1 << i))
			cout << "1";
		else
			cout << "0";

	// cout << "\n";
}

void solve()
{
	rep(i, (1 << (n-2)))
	{
		LL cur = (1 << (n-1)) + 1 + (i << 1);
		// cout << cur <<"\n";
		// writeOut(cur);
		bool tr = false;
		for(int j = 2; j <= 10; j++)		
			if (!checkSys(cur, j))
				tr = true;

		if (!tr)
		{
			// cout << cur << "\n";
			res.pb(cur);
			writeOut(cur);
			for(int j = 2; j <= 10; j++)
				cout << " " << checkSys(cur, j);
			cout << "\n";
		}


		if((int)res.size() >= k)
			break;

	}
// 
	// rep(i, k)
		// writeOut(i);
}


int main()
{
	cin >> t;
	// t = 1;
	// cout <<  divisor(4) <<"\n";
    rep(i,t)
    {
    	cout << "Case #" << i + 1 << ":\n";
        // genPrimes();
        readIn();
        solve();
    }

    return 0;
}
