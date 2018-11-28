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
struct pass{
	int s,cnt;
	friend bool operator<(pass a,pass b) { return (a.s!=b.s?a.s<b.s:a.cnt>b.cnt); }
}p[MAX+10];
int n,m;

int main()
{
	ios::sync_with_stdio(false);
	int tests;
	cin >> tests;
	for(int tt=0; tt<tests; tt++)
	{
		cin >> n >> m;
		ll all = 0;
		for(int i=0; i<m; i++)
		{
			cin >> p[2*i].s >> p[2*i+1].s >> p[2*i].cnt;
			p[2*i].s--, p[2*i+1].s--;
			p[2*i+1].cnt = -p[2*i].cnt;
			all += ( 2 * n + p[2*i].s - p[2*i+1].s + 1 ) * (ll)( p[2*i+1].s - p[2*i].s ) * p[2*i].cnt / 2;
			all %= D;
		}
//		cerr << all << endl;
		sort( p , p+2*m );
		
		map<int,int> mp;
		int last = 0;
		ll sum = 0;
		for(int i=0; i<2*m; i++)
		{
//			cerr << "/---------:\n";
//			cerr << p[i].s << " " << p[i].cnt << endl;
			if( last != p[i].s )
				foreach(it,mp)
				{
//					cerr << it->F << " " << it->S << endl;
					sum += ( 2 * it->F - last - p[i].s + 1 )*(ll)( p[i].s - last ) * it->S / 2;
//					cerr << sum << endl;
					sum %= D;
				}
			last = p[i].s;
			
			if( p[i].cnt > 0 )
				mp[n+p[i].s] += p[i].cnt;
			else
			{
				map<int,int>::iterator it = mp.end();
				it--;
				while( p[i].cnt < 0 )
				{
					if( it->S > -p[i].cnt )
					{
						it->S += p[i].cnt;
						p[i].cnt = 0;
					}
					else
					{
						map<int,int>::iterator it2 = it--;
						p[i].cnt += it2->S;
						mp.erase(it2);
					}
				}
			}
		}
		cout << "Case #" << tt+1 << ": " << ((all-	sum)+D)%D << endl;
	}
	//cerr << "Time :  " << (double)clock() / CLOCKS_PER_SEC << endl;
	return 0;
}













