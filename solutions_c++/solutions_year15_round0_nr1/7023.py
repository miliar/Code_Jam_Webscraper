/**
	* Author	: Arif Ahmad
	* Date		:
	* Algorithm	:
	* Difficulty:
*/

#include <bits/stdc++.h>
using namespace std;

#define INF_MAX 	2147483647
#define INF_MIN 	-2147483648
#define INF 		(1 << 30)
#define EPS			1e-9
#define PI 			acos(-1.0)
#define N 		    2 + 10000
#define MOD			10000000007
#define sz(x) 		(int)(x).size()
#define all(x) 		(x).begin(), (x).end()
#define pb 			push_back
#define mp			make_pair
#define ms(x, a) 	memset((x), (a), sizeof(x))
#define F           first
#define S           second
#define rep(i,a,b)  for(int i=(a); i<(b); ++i)
#define repC(i,x) 	for(size_t i=0; i<x.size(); ++i)
#define repIT(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define nn          '\n'

typedef long long 		LL;
typedef pair<int,int> 	pii;
typedef vector<int> 	vi;
typedef vector<string> 	vs;
typedef vector<char>	vc;
typedef vector<bool>    vb;
typedef vector< pii >   vii;
typedef map<string,int> msi;
typedef map<int,int>	mii;
typedef map<char,int>   mci;
typedef map<int,string>	mis;

template<class T> T Abs(T x) {return x>0 ? x : -x;}
template<class T> T Max(T a, T b) {return a>b ? a : b;}
template<class T> T Min(T a, T b) {return a<b ? a : b;}
template<class T> T gcd(T a, T b) {return (b ? gcd(b,a%b) : a);}
bool isVowel(char ch){ch=tolower(ch);return(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u');}

//int dx[4] = {-1, 0, 0, 1};
//int dy[4] = {0, -1, 1, 0};
//int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
//int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};


int main()
{
    ios_base :: sync_with_stdio(0);
    cin.tie(0);

	#ifndef ONLINE_JUDGE
		//freopen("in.txt", "r", stdin);
		//freopen("A-small-attempt0.in", "r", stdin);
		freopen("A-large.in", "r", stdin);
		freopen("a_out.txt", "w", stdout);
	#endif

	int i, j, k, n, tc;
	int sMax;
	string s;

    cin >> tc;
	rep(cn, 1, tc+1)
	{
	    cin >> sMax >> s;

	    n = sMax + 1;
	    int total = s[0] - '0', needed = 0;
	    rep(i, 1, n)
	    {
	        k = s[i] - '0';
	        if(k == 0) continue;
	        if(total < i) {
                needed += (i - total);
                total = i;
	        }
	        total += k;
	    }

        cout << "Case #" << cn << ": " << needed << nn;
	}

	return 0;
}
