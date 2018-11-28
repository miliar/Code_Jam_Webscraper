#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cmath>
#include <list>
#include <cstdlib>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define FOR(i,a,b)  for(int (i) = (a);(i)<(b);(i)++)
#define   REP(i,n) FOR(i,0,n)
#define  INF (1<<29)
#define         pb push_back
#define 	     sz size()
#define         mp make_pair
#define all(a) a.begin(),a.end()
#define SI(n)               scanf("%d",&n);
#define SL(n)               scanf("%lld",&n);
#define fill(ar,val) memset(ar,val,sizeof ar)
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define fi first
#define se second
typedef long long ll;
typedef pair<int,int>  pii;
typedef vector<string> vs;
ll s2i(string s) { istringstream iss(s); ll x;iss>>x; return x;}
string i2s(ll x) { ostringstream oss; oss<<x; return oss.str();}


int chk( int a)
{
	string s;
	stringstream ss;
	ss << a;
	ss >> s;
	//cout <<s << endl;
	int flag = 1;
	for( int i = 0; i < s.size()/2;i++) {
		if ( s[i] != s[s.size()-1-i]) {
			flag = 0;
			break;
		}
	}
	return flag;

}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
freopen("output1.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	int c = 1;
	int a,b;
	while( t--) {
		cin >> a >> b;
		int count = 0;
		for ( int i = a; i <= b; i++) {
			if ( chk(i) ) {
				int q = sqrt(i);
				if( q*q == i && chk(q) == 1) {
					count++;
					//cout << i << endl;
				}
			}
		}
		cout <<"Case #"<<c<<": "<< count << endl;
		c++;
	}
	return 0;
}	
