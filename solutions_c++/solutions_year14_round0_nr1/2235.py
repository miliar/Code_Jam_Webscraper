#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
using namespace std;
#define TR(i,v) 		for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x) 		cout << #x << " = "; cout << x << endl;
#define SIZE(p) 		(int)(p).size()
#define MP(a, b)		make_pair((a), (b))
#define ALL(p)			(p).begin(), (p).end()
#define rep(i, n)		for(int (i)=0; (i)<(int)(n); ++(i))
#define REP(i, a, n)	for(int (i)=(a); (i)<(int)(n); ++(i))
#define FOR(i, a, b)   	for(int (i)=(int)(a); (i)<=(int)(b); ++(i))
#define FORD(i, b, a)  	for(int (i)=(int)(b); (i)>=(int)(a); --(i)) 
typedef long long LL;
typedef pair<int, int> pii;
int A[5][5], B[5][5];
inline bool ok(int x, int r1, int r2)
{
	int c1=-1, c2=-1;
	FOR(i, 1, 4)
	FOR(j, 1, 4)	if(A[i][j]==x)
		c1=i;
	FOR(i, 1, 4)
	FOR(j, 1, 4)	if(B[i][j]==x)
		c2=i;
	return c1==r1 && c2==r2;
}
int main(int argc, char const *argv[])
{
	// #ifndef ONLINE_JUDGE
 //    freopen("A.in", "r", stdin);
 //    freopen("A.txt", "w", stdout);
 //    #endif
	// ios::sync_with_stdio(false);		cin.tie(0);
    int T;			scanf("%d", &T);
    FOR(cs, 1, T)
    {
    	int r1;		scanf("%d", &r1);
    	FOR(i, 1, 4)
    	FOR(j, 1, 4)
    		scanf("%d", &A[i][j]);
    	int r2;		scanf("%d", &r2);
    	FOR(i, 1, 4)
    	FOR(j, 1, 4)
    		scanf("%d", &B[i][j]);
    	vector<int> R;
    	FOR(i, 1, 16)	if(ok(i, r1, r2))
    		R.push_back(i);
    	printf("Case #%d: ", cs);
    	if(R.empty())		puts("Volunteer cheated!");
    	if(SIZE(R)>1)		puts("Bad magician!");
    	if(SIZE(R)==1)		printf("%d\n", R[0]);
    }
	return 0;
}