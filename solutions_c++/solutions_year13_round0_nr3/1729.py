#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define mset(mas,val) memset(mas,val,sizeof(mas))
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
	
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

long long good[] = {1ll,4ll,9ll,121ll,484ll,10201ll,12321ll,14641ll,40804ll,44944ll,1002001ll,1234321ll,4008004ll,100020001ll,
	102030201ll,104060401ll,121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll,
	12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,
	1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};
                                                                                    
int main(){
#ifdef gridnevvvit
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int testcases;
	cin >> testcases;
	int testcount = 1;
	while (testcases--) {
		long long A, B;
		cin >> A >> B;
		int ans = 0;
		for(int i = 0; i <= 38; i++)
			if (good[i] >= A && good[i] <= B)
				++ans;
		printf("Case #%d: %d\n", testcount++, ans);
	}
}