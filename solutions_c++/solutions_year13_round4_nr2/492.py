#include<iostream>
#include<algorithm>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<ctime>
#include<set>
#include<map>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> PII;
typedef pair<ld,ld> PDD;

#define U adj[v][i]
#define N(x) ((int)adj[x].size())
#define all(x) x.begin() , x.end()
#define F first
#define S second
#define X first
#define Y second
#define show(x) cerr << #x << " " << x << " " << endl;
#define Heap(x) priority_queue<x,vector<x>,greater<x> >
#define foreach(it,s) for(__typeof(s.begin())it=s.begin(); it!=s.end(); it++)

template<class P,class Q> void mins(P& a,Q b) { a = min( a , (P)b ); }
template<class P,class Q> void maxs(P& a,Q b) { a = max( a , (P)b ); }

const int MAX = 1000+1;
const int INF = 1<<29;
const ll D = 1000002013;
int n;
ll p;

ll find1()
{
	for(int i=n-1; i>=0; i--)
		if( p <= (1ll<<i) )
			return (1ll<<(n-i));
		else
			p -= 1ll<<i;

	return (1ll<<n)+1;
}

ll find2()
{
	int cnt = 0;
	for(int i=n; i>0; i--)
		if( ( p&(1ll<<i) ) == 0 )
			cnt++;
		else
			break;
	
	return (1ll<<n) - (1ll<<cnt);
}

int main()
{
	ios::sync_with_stdio(false);
	int tests;
	cin >> tests;
	for(int tt=0; tt<tests; tt++)
	{
		cin >> n >> p;
		cout << "Case #" << tt+1 << ": " << find1()-1-1 << " " << find2() << endl;
	}
	//cerr << "Time :  " << (double)clock() / CLOCKS_PER_SEC << endl;
	return 0;
}













