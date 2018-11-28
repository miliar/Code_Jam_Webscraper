/* k_____k */

#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
#include<cctype>
#include<cassert>
#include<climits>
#include<cerrno>
#include<cfloat>
#include<ciso646>
#include<clocale>
#include<csetjmp>
#include<csignal>
#include<cstdarg>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cwchar>
#include<cwctype>

//containers
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<complex>
#include<string>
#include<stack>
#include<bitset>
#include<istream>
#include<valarray>

//IOs
#include<iostream>
#include<sstream>
#include<iomanip>
#include<fstream>
#include<exception>
#include<ios>
#include<iosfwd>
#include<ostream>
#include<iterator>
#include<stdexcept>
#include<streambuf>


//algorithm & miscellaneous
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<limits>
#include<locale>
#include<memory>
#include<new>

// My Terms
#define pb push_back
#define mp make_pair
#define ins insert
#define fir first
#define sec second
#define PRINT(x)        cout << #x << " " << x << endl
#define pi acos(-1)
#define ll long long
#define EM empty()
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define fill(a,v)     memset(a, v, sizeof(a))

using namespace std;

unsigned long long mod=1000000007;

ll a,b;
int cnt;
ll arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,
125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,
1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,
4004009004004,100000020000001};
void check(){
	for(int i=0;i<40;i++)
		if(arr[i]>=(ll)a and arr[i]<=(ll)b)
			cnt++;
	return ;
}
int main(){
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++){
		cnt=0;
		cin>>a>>b;
		check();
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}


/*
This isn't my field,
still i code to show,
anyone can do it ^_^
*/


