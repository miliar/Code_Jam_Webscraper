#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<limits.h>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
typedef vector<int> vi;
typedef vector<bool> vb;
#define rep(i,n,m) for( int i = (int)(n), _m = (int)(m) ; i < _m ; ++i )
#define	rrep(i,n,m) for( int i = (int)(n), _m = (int)(m) ; i >= _m ; --i )
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define pb(x) push_back(x)
#define mp make_pair
#define mems(arr, v) memset(arr, v, sizeof arr)
#define setb(mask, bit) ((mask)|((1LL)<<(bit)))
#define resetb(mask, bit) ((mask)&(~((1LL)<<(bit))))
#define is0(mask, bit)(((mask)&((1LL)<<(bit)))==0)
#define is1(mask, bit)(((mask)&((1LL)<<(bit)))!=0)
#define INT_MAX  2000000000
#define INT_MIN -INT_MAX
#define EPS 1e-1
#define debug(x) cout << #x << " : " << x << endl
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define Read() freopen("in.in","r",stdin)
#define Write() freopen("out.txt","w",stdout)
int main()
{
	Read();
	Write();
	ull nums[48] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321,400000080000004};
	int t;
	cin>>t;
	ull a,b;
	rep(test, 1, t+1)
	{
		cin>>a>>b;
		int c = 0;
		rep(i,0,48)
			if(nums[i]<=b&&nums[i]>=a)
				c++;
		cout<<"Case #"<<test<<": "<<c<<endl;
	}
}