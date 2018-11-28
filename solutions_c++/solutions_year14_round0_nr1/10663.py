#include <algorithm>
#include <cassert>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;
/*========================================Templates=============================================*/
// datatypes
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double db;
typedef float ft;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
int gcd( int a, int b ) {  if( !b ) return a;  return gcd( b, a % b ); }

#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define tests(tc) int tc;scanf("%d",&tc);while(tc--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR1(i,a,b) for(int i=(a);i<(b);++i)
#define FORN(i,a,b,n) for(int i=(a);i<=(b);i+=n)
#define FORR(i,a,b) for(int i=(a);i>=(b);--i)
#define FORRN(i,a,b,n) for(int i=(a);i>=(b);i-=n)
#define CLEAR(arr,v)        memset(arr,v,sizeof(arr))
#define INF ((1<<30)-1)


#define DEBUG
#ifdef DEBUG
#define DB(x) cerr<<#x<<" : "<<x<<endl<<flush;
#define DB2(x,y) cerr<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<endl<<flush;
#define DB3(x,y,z) cerr<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<" "<<#z<<" : "<<z<<endl<<flush;
#define DB4(w,x,y,z) cerr<<#w<<" : "<<w<<" "<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<" "<<#z<<" : "<<z<<endl<<flush;
#define DB5(v,w,x,y,z) cerr<<#v<<" : "<<v<<" "<<#w<<" : "<<w<<" "<<#x<<" : "<<x<<" "<<#y<< \
	" : "<<y<<" "<<#z<<" : "<<z<<endl<<flush;
#define DBAR(arr,a,b) cerr<<#arr<<" : ";FOR(dbar,a,b) cerr<<arr[dbar]<<" ";cerr<<endl;
#define DBAR2(arr,a,b,x,y) cerr<<#arr<<endl;FOR(dbar,a,b){ FOR(dbar2,x,y)cerr<<arr[dbar][dbar2]<<" ";cerr<<endl;}

#else
#define DB(x)
#define DB2(x,y)
#define DB3(x,y,z)
#define DB4(w,x,y,z)
#define DB5(v,w,x,y,z)
#define DBAR(arr,a,b)
#define DBAR2(arr,a,b,x,y)
#endif

/*======================================Templates Ends========================*/
/* Main Code Starts from here */

int main() {

	int kase = 1;
	int num;

	tests(tc) {
		int a,b;
		vector<int> vi[10];
		scanf("%d", &a);
		FOR(i,1,4)
			FOR(j,1,4) {
				scanf("%d", &num);
				vi[i].push_back(num);
			}
		scanf("%d", &b);
		b += 4;
		FOR(i,5,8)
			FOR(j,1,4) {
				scanf("%d", &num);
				vi[i].push_back(num);
			}

		vector<int>::iterator it;
		vector<int> v(10);
		sort(vi[a].begin(), vi[a].end());
		sort(vi[b].begin(), vi[b].end());
		it=std::set_intersection (vi[a].begin(), vi[a].end(), vi[b].begin(), vi[b].end(), v.begin());
        v.resize(it-v.begin());

        if(v.size() == 0) {
        	printf("Case #%d: Volunteer cheated!\n", kase++);
        }
        else if(v.size() > 1) {
        	printf("Case #%d: Bad magician!\n", kase++);
        }
        else {
        	printf("Case #%d: %d\n", kase++, v[0]);
        }

	}
	return 0;
}

