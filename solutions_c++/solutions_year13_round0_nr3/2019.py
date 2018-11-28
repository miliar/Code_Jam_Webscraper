#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>

#define inf (1<<30)
#define eps 1e-5
#define ll long long
#define all(v)  v.begin() , v.end()
#define sc(x) scanf("%d",&x)
#define me(t,val) memset( t , val , sizeof(t) )

#define N 39
#define MOD 1000000007

using namespace std;

ll a[] = { 1LL , 4LL , 9LL , 121LL , 484LL , 10201LL , 12321LL , 14641LL , 40804LL , 44944LL , 1002001LL , 1234321LL , 4008004LL , 100020001LL , 102030201LL , 104060401LL , 121242121LL , 123454321LL , 125686521LL , 400080004LL , 404090404LL , 10000200001LL , 10221412201LL , 12102420121LL , 12345654321LL , 40000800004LL , 1000002000001LL , 1002003002001LL , 1004006004001LL , 1020304030201LL , 1022325232201LL , 1024348434201LL , 1210024200121LL , 1212225222121LL , 1214428244121LL , 1232346432321LL , 1234567654321LL , 4000008000004LL , 4004009004004LL };
int main()
{
	int tc;
	cin >> tc;
	for( int t = 0 ; t < tc ; ++t )
	{
		ll A , B;
		cin >> A >> B;
		cout << "Case #" << t + 1 <<": " << upper_bound( a , a + N , B ) - upper_bound( a , a + N , A - 1 ) << endl;	
	}
}
