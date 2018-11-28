/**
	* Author: Arif
	* Date:
*/

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <iomanip>
using namespace std;

#define INF_MAX 	2147483647
#define INF_MIN 	-2147483648
#define INF 		(1 << 30)
#define EPS			1e-7
#define PI 			acos(-1.0)
#define N 		    2 + 1000000
#define MOD			10000000007
#define sz(x) 		(int)(x).size()
#define all(x) 		(x).begin(), (x).end()
#define pb 			push_back
#define mp			make_pair
#define ms(x, a) 	memset((x), (a), sizeof(x))
#define F           first
#define S           second
#define rep(i,a,b)  for(int i=(a); i<(b); i++)
#define repC(i,x) 	for(size_t i=0; i<x.size(); i++)
#define repIT(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long 		LL;
typedef pair<int,int> 	pii;
typedef vector<int> 	vi;
typedef vector<string> 	vs;
typedef vector<char>	vc;
typedef vector<bool>    vb;
typedef map<string,int> msi;
typedef map<int,int>	mii;
typedef map<char,int>   mci;
typedef map<int,string>	mis;

template<class T> T Abs(T x) {return x>0 ? x : -x;}
template<class T> T Max(T a, T b) {return a>b ? a : b;}
template<class T> T Min(T a, T b) {return a<b ? a : b;}
template<class T> T gcd(T a, T b) {return a%b==0 ? b : gcd(b,a%b);}
bool isVowel(char ch){ch=tolower(ch);return(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u');}


int main()
{
	#ifndef ONLINE_JUDGE
		//freopen("in.txt", "r", stdin);
		freopen("B-small-attempt0.in", "r", stdin);
		//freopen("in.txt", "r", stdin);
		freopen("bout_small.txt", "w", stdout);
		//freopen("bout_large.txt", "w", stdout);
	#endif

	int i, j, k, n, tc;
    double c, f, x, p, t1, t2, ans;

    cin >> tc;
	rep(cn, 1, tc+1)
	{
	    cin >> c >> f >> x;

	    p = 2;
	    ans = 0;
	    while(1)
        {
            t1 = (c / p) + (x / (p+f));
            t2 = x / p;
            if(t1+EPS < t2)
            {
                ans += (c / p);
                p += f;
            }
            else
            {
                ans += t2;
                break;
            }
        }

        cout << "Case #" << cn << ": ";
        //cout << ans << endl;
        printf("%.7f\n", ans);

	}

	return 0;
}
