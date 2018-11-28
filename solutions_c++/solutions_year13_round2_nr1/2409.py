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

vi v;

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("A-small-attempt4.in", "r", stdin);
		freopen("a_out.txt", "w", stdout);
	#endif

	int i, j, k, n, tc;
    LL a, b;

    cin >> tc;
	rep(cn, 1, tc+1)
	{
	    cin >> a >> n;

	    v.clear();
	    rep(i, 0, n)
	    {
	        cin >> k;
	        v.pb(k);
	    }
	    sort(all(v));

	    int ans = 0, cnt, lim;
	    bool done = false;
	    repC(i, v)
	    {
	        if(v[i] < a) a += v[i];
	        else
            {
                b = a;
                cnt = 0;
                lim = sz(v) - i; //cerr<<"lim: "<<lim<<endl;
                done = false;
                while(b <= v[i])
                {
                    b = b + (b - 1);
                    cnt++;
                    if(cnt >= lim)
                    {
                        ans += lim;
                        done = true;
                        break;
                    }
                }
                if(!done)
                {
                    //cerr<<"here"<<endl;
                    ans += cnt;
                    a = b + v[i];
                }
            }
            if(done) break;
	    }

        printf("Case #%d: %d\n", cn, ans);
	}

	return 0;
}
