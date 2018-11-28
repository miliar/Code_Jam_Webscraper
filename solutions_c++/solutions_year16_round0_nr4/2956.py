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
int n,m,k,l, t = 1, c, s;
const int inf = 1000 * 1000 * 1000 ;
const int MAKSN = 1000 * 1000 + 13; // UZUPElnic



void readIn()
{
	cin >> k >> c >> s;
}


void solve()
{	
	rep(i, s)
		cout << i + 1 << " ";
	cout << "\n";
}


int main()
{
	cin >> t;
    rep(i,t)
    {
    	cout << "Case #" << i + 1 << ": ";
        readIn();
        solve();
    }

    return 0;
}
