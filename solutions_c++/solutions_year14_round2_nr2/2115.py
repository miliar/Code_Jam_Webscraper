//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)

//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
  int test,t,a,b,k,count_=0;
  cin >> test;
  t = test;
  while(test--)
  {
    cin >> a >> b >> k;
    count_=0;
    repi(i,0,a)
    	repi(j,0,b)
    	{
    		if((i&j) < k)
    			count_++;
    	}
    printf("Case #%d: %d\n",t-test,count_);
  }
  return 0;
}