#include <algorithm> 
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector> 
using namespace std;

typedef long long             ll;
typedef vector<int>           vi;
typedef pair<int, int>        ii;
typedef vector<ii>            vii;
typedef map<int, int>         mii;
typedef set<int>              si;
typedef map<string, int>      msi;
typedef vector<bool>          vb;
typedef long double           ld;

#define rep(i, a, b)    for (long long int i = int(a); i <= int(b); i++)
#define repd(i, a, b)   for (int i = int(a); i >= int(b); i--)
//#define TR(c, it)       for (typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pb              push_back
#define mp              make_pair
#define SIZE(c)         (int((c).size()))
#define LET(x, a)       __typeof(a) x = (a)
#define FOR(x, a, b)    for(LET(x,a); x!=(b); x++)
#define TR(cnt, it)     FOR(it, (cnt).begin(), (cnt).end())
 
#define vsort(v)        sort(v.begin(), v.end())
#define REDIRECT_INPUT  freopen("input.txt", "r", stdin)
#define REDIRECT_OUTPUT freopen("output.txt","w", stdout);
#define INF 2147483647  // 2^31-1

bool ispalindrome(long long num)
{
	long long n = num;
	long long rev = 0;
	int dig;
	while (num > 0)
	{
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
	}
	if(n == rev)
	return true;
	else
	return false;
}
int case1;
int main()
{
	REDIRECT_INPUT;
	REDIRECT_OUTPUT;
	int T;
	cin >> T;
	case1 = 1;
	long long lower,higher,m,n,square;
	if(ispalindrome(2))
	//cout<<"hetttttttttttttt";
	//T = 0;
	while(T--)
	{
		int count = 0;
		cin >>lower>>higher;
		//cout<<lower<<higher;
		n = (long long)sqrt((double)lower);
		m = (long long)sqrt((double)higher);
		//cout<<"LOWER   "<<n<<"Higher  "<<m;
		rep(i,n-1,m+1)
		{
			if(ispalindrome(i))
			{
				//cout<<"is palindrome    "<< i <<'\n';
				square = i*i;
				if(ispalindrome(square) && square>=lower && square<=higher)
				{
					//cout<<"My numberrrr "<<square<<"     "<<i<<'\n';
					count++;
				}
			}
		}
       cout<<"Case #"<<case1<<": "<<count<<'\n';
       case1++;
 }      
}
