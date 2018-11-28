#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
const int MOD =1e9 + 7;
const int INF = 0x3f3f3f3f;

const int MXN=1e7+1;
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
LL Ans[]={0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int Fun(LL x)
{
	return upper_bound(Ans,Ans+40,x)-Ans;
}
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int kas=1;kas<=T;++kas)
	{
		LL a,b;
		scanf("%lld%lld",&a,&b);
		printf("Case #%d: %d\n",kas,Fun(b)-Fun(a-1));
	}
	
	return 0;
}
