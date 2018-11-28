#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define lld long long int 
#define EOL '\0'

#define N 102
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(n) for(int i =0;(i)<(int)(n);(i)++)
#define repi(n) for(int i =0;(i)<(int)(n);(i)++)
#define repj(n) for(int j =0;(j)<(int)(n);(j)++)
#define repij(n,m) for(int i =0;(i)<(int)(n);(i)++) for(int j =0;(j)<(int)(m);(j)++)
#define rep1n(n) for(int i=1;i<(int )(n);i++)

#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
                  std::ostringstream() << std::dec << x ).str()


using namespace std;



bool ispalin(string s) {
	int i,j;
	for(i=0,j=s.length()-1;i<=j && s[i]==s[j];i++,j--);
	return i>j;
}

unsigned lld fs[] = 
	{
		 1,
 4,
 9,
 121,
 484,
 10201,
 12321,
 14641,
 40804,
 44944,
 1002001,
 1234321,
 4008004,
 100020001,
 102030201,
 104060401,
 121242121,
 123454321,
 125686521,
 400080004,
 404090404,
 10000200001,
 10221412201,
 12102420121,
 12345654321,
 40000800004,
 1000002000001,
 1002003002001,
 1004006004001,
 1020304030201,
 1022325232201,
 1024348434201,
 1210024200121,
 1212225222121,
 1214428244121,
 1232346432321,
 1234567654321,
 4000008000004,
 4004009004004
	};


int main() 
{
	int n;
	unsigned lld a,b;
	freopen("C:\\MyCode\\jam\\Data\\C-large-1.in", "r",stdin);
	freopen	("C:\\MyCode\\jam\\Data\\C-large-1.out", "w",stdout);
	cin>>n;
	rep(n) {
		cin>>a>>b;
		int ac = 0 , bc = 0;
		repj(39)
			ac += fs[j] < a ? 1 :0,
			bc += fs[j] <=b ? 1 :0;
		cout<<"Case #"<<i+1<<": "<<bc-ac<<endl;
	}
			
	return 0;
}