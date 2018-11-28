//#includes {{{
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <complex>
#include <list>
#include <stack>
#include <queue>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;
// }}}
// #defines {{{
#define sz(a) int((a).size())
#define pb push_back

#define all(c) (c).begin(),(c).end()
#define FOR(i,a,b) for (int i=a; i<(int(b)); i++)
#define tr(it, container) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;

template<class T>
void splitline(const string &s, vector<T> &dest) {
    istringstream in(s);
    dest.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(dest));
}
template<class T>
inline void PRINT_ELEMENTS(const T& coll, const char* optcstr=""){
    typename T::const_iterator pos;
    std::cout<< optcstr;
    for(pos=coll.begin();pos!=coll.end();++pos){
        cout << *pos << ' ';
    }
    cout << endl;
}
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
int s2i(string str){
    stringstream ss; int n;
    ss << str; ss >> n; return n; }
string i2s(int n){
stringstream ss; string str;
ss << n; ss >> str; return str; }
// }}}

ll issquare(ll a){
    if(a==1) return 1;
    ll x = a/2;
    vector<ll> b; b.clear();
    b.pb(x);
    while(x*x!=a){
        x= (x + a/x)/2;
        if(find(all(b),x)!=b.end()) return -1;
        b.pb(x);
    }
    return *(b.end()-1);
}
bool ispal(ll num){
     ll n = num;
     ll rev =0;
     while (num > 0) {
      int d = num%10;
      rev = rev*10+d;
      num = num / 10;
     }
   return  (n == rev);
}
int main(int argc, char*argv[]){
    //codejam
    int t;
    scanf("%d\n",&t);
    for(int z=0;z<t;z++) {
        ll a,b;
        scanf("%Ld %Ld",&a,&b);
        ll ctr=0;
        for(ll i=a;i<=b;i++){
            if(ispal(i)){
            if( issquare(i)!=-1 && ispal(issquare(i))) {
             ctr++;
            }
            }
        }
        printf("Case #%d: ",z+1);
        printf("%Ld",ctr);
        printf("\n");
    }
}

// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

