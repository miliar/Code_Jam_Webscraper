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
#include <cstring>
/*#include <hash_map>
using namespace __gnu_cxx;*/
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

ll MX = 100000000;
bool isFairPal(ll n) {
	ll sq = n*n;
	vector<int>v1, v2;
	while(n)
		v1.pb(n%10), n/=10;
	while(sq)
		v2.pb(sq%10), sq/=10;

	for (int i = 0; i < (int)v1.size(); ++i)
		if(v1[i] != v1[v1.size()-1-i])
			return false;
	for (int i = 0; i < (int)v2.size(); ++i)
		if(v2[i] != v2[v2.size()-1-i])
			return false;

	return true;

}
ll fPal[] = {1LL, 4LL, 9LL, 121LL, 484LL, 10201LL, 12321LL, 14641LL, 40804LL, 44944LL, 1002001LL, 1234321LL, 4008004LL, 100020001LL, 102030201LL, 104060401LL, 121242121LL, 123454321LL, 125686521LL, 400080004LL, 404090404LL, 10000200001LL, 10221412201LL, 12102420121LL, 12345654321LL, 40000800004LL, 1000002000001LL, 1002003002001LL, 1004006004001LL, 1020304030201LL, 1022325232201LL, 1024348434201LL, 1210024200121LL, 1212225222121LL, 1214428244121LL, 1232346432321LL, 1234567654321LL, 4000008000004LL, 4004009004004LL, 100000020000001LL, 100220141022001LL, 102012040210201LL, 102234363432201LL, 121000242000121LL, 121242363242121LL, 123212464212321LL, 123456787654321LL, 400000080000004LL };
const int MXX = 47;
int main() {
	//	std::ios_base::sync_with_stdio(false);
	freopen("C-large-1.in", "rt", stdin);
	freopen("C-large1.txt", "wt", stdout);

	int t;
	cin>>t;
	ll a, b;

	for (int ii = 0; ii < t; ++ii) {
		cin>>a>>b;
		int cnt = 0;
		for (int i = 0; i < MXX; ++i) {
			if(fPal[i]>=a && fPal[i]<=b)
				++cnt;
		}
		cout<<"Case #"<<ii+1<<": "<<cnt<<endl;
	}
	return 0;
}
