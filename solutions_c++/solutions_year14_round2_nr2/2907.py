#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <numeric>
#include <functional>
#include <string>
#include <cstring>
#include <stack>
#include <queue>

#define vi vector<int>
#define vvi vector< vectort<int> >
#define pii pair<int, int>
#define vpii vector<pii>
#define mii map<int, int>
#define rep(i, n) for(int i = 0; i < (n); ++i)
#define f(i, a, b) for(int i =(a); i < (b); ++i)
#define fd(i, a, b) for(int i = (a); i >= (b); --i)
// #define prv(v) for(typeof(int) i = 0; i < sizeof(v)/sizeof(*v); ++i) cout << *(v+i) << " "; cout<<endl
#define prv(v) for(auto i = 0; i < sizeof(v)/sizeof(*v); ++i) cout << *(v+i) << " "; cout<<endl

// #define fc(it, c) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define fc(it, c) for(auto it = (c).begin(); it!=(c).end(); it++)
#define prc(c) for(auto i = (c).begin(); i !=(c).end(); i++ ) cout << *i << " "; cout<<endl
// #define prc(c) for(typeof((c).begin()) i = (c).begin(); i !=(c).end(); i++ ) cout << *i << " "; cout<<endl
#define all(c) (c).begin(), (c).end()
#define allr(c) (c).rbegin(), (c).rend()
#define present(c, e) ((c).find(e) != (c).end())//set/map,etc
#define presentc(c, e) ((c).find(all(c), e) != (c).end())//vector

typedef long long ll;
#define szc(c) int((c).size())
#define szv(v) sizeof(v)/sizeof(v[0])
#define pb(x) push_back(x)
#define print(x) cout << x << endl

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
using namespace std;

long long mod = 1e9 + 7;

int main(int argc, const char *argv[])
{
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	int A, B, K;
	int sol;
	cin >> T;

	f(i, 1, T+1) {
		sol = 0;
		cin >> A >> B >> K;
		f(j, 0, A) {
			f(k, 0, B) {
				if((j&k) < K)
// 					cout << (j&k) << endl;
					sol++;
			}
		}
		printf("Case #%d: %d\n", i, sol);
	}
	return 0;

}

