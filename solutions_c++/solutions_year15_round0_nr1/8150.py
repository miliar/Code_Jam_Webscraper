// Author: Pulkit Yadav

#include <vector>
#include <cstring>
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
#include <limits>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define sz(a)                       ((int)(a.size()))
#define forall(i,a,b)               for(int i=(a);i<(long long)(b);i++)
#define forinv(i,h,l)               for(int i=(h);i>=(long long)(l);i--)
#define tr(it, c)                   for( __typeof__( (c).begin()) it = (c).begin();  it != (c).end(); ++it)
#define fill(a,v)                   memset(a, v, sizeof a)
#define all(a)                      a.begin(), a.end()
#define IND(A,v)                    (std::find(all(A),v)-A.begin())
#define in(A,v)                     (std::find(A.begin(), A.end(), v) != A.end())
#define bitcount                    __builtin_popcount
#define D(v)                        cout<< #v" : " << v << "\n";
#define DA(a,n)                     {cout<<#a": [";forall(i,0,n)cout<<a[i]<<" ";cout<<"]\n";}
#define oo                          (int)(1e9+10)
#define EPS                         (1e-9)
#define S(n)                        scanf("%d",&n)
#define INITFROMARR(arr)            (arr, arr + sizeof(arr)/sizeof(arr[0]))
#define GCD(a,b)                    (abs(__gcd(a,b))
#define MP                          make_pair
#define PB                          push_back

template <class T> string to_s(const T& a) {ostringstream os; os<<a; return os.str();}
template <class T> T to_T(const string& s) {istringstream is(s); T r; is>>r; return r;}
//e

int main(){
	int t;
	cin >> t;

	forall(cs, 1, t+1){
		int standing = 0, ans = 0, smax, si;
		cin >> smax;
		string nums;
		cin >> nums;
		forall(i, 0, smax+1){
			int ni = to_T<int>(string(1, nums[i]));
			if(standing < i && ni > 0){
				ans += (i-standing);
				standing += (i-standing);
			}
			standing += ni;
		}
		cout << "Case #" << cs << ": " << ans << endl;
	}
	return 0;
}