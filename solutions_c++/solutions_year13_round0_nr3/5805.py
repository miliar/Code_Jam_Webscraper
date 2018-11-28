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
#define EPS			1e-9
#define PI 			acos(-1.0)
#define N 		    2 + 100
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

int res[N];

bool isPalindrome(int n)
{
    int a=n, b=0;

    while(n)
    {
        b *= 10;
        b += n % 10;
        n /= 10;
    }

    return a==b;
}

void memo()
{
    int id = 0;
    rep(i, 1, 1001)
    {
        if(isPalindrome(i))
        {
            int j = i * i;
            if(isPalindrome(j))
                res[id++] = j;
        }
    }

    // test
    id = 0;
    //while(res[id]) cerr<<res[id++]<<" ";
}


int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("c_out.txt", "w", stdout);
	#endif

	int i, j, k, n, tc, a, b;

    memo();

    cin >> tc;
    rep(cn, 1, tc+1)
	{
	    cin >> a >> b;

	    int ans = 0;
	    for(i=0; res[i]<=b; i++)
        {
            if(res[i] >= a && res[i] <= b) ans++;
        }

        printf("Case #%d: %d\n", cn, ans);
	}

	return 0;
}
