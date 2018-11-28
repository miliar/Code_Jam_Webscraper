#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <streambuf>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>

#define all(x) (x).begin(),(x).end() 
#define sz(v) ((int) v.size())
#define mp make_pair 
#define fori(type,x,a,b) for( type (x) = (a) ; (x) < (b) ; (x)++) 
#define forr(type,x,a,b) for( type (x) = (a) ; (x) >= (b) ; (x)--) 
#define fi(x,a,b) fori(int,x,a,b) 
#define fri(x,a,b) forr(int,x,a,b) 
#define fll(x,a,b) fori(long long,x,a,b) 
#define frll(x,a,b) forr(long long,x,a,b) 
#define fill(x,v,n) memset((x),(v),n*sizeof(x)); 
#define pb(x) push_back(x)

#define p(x) cout << x << " "
#define pl cout << endl
#define pn(x) cout << #x <<": "<< x << endl

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#if 1
bool isPalin(int n)
{
	int rev = 0, num = n;
	while (num)
	{
		rev = rev*10 + num%10;
		num/=10;
	}
	return rev == n;
}
int fairAndSquare(int left, int right)
{
	int ans = 0;
	fi(num, left, right+1)
	{
		int sqroot = sqrt(num*1.0);
		// if n is a perfect square
		if(isPalin(num) && sqroot * sqroot == num)
		ans += isPalin(sqroot);
	}
	return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
#endif
	int n;
	cin>>n;

	fi(i,0,n)
	{
		int left, right;
		cin>>left>>right;

		cout<<"Case #"<<i+1<<": "<<fairAndSquare(left, right)<<endl;
	}

	return 0;
}
#endif
