#include <vector>
#include <list>
#include <map>
#include <set>
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
 
using namespace std;
 
#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;
#define EPS 1e-12

vector<int> v;

int rev(int number){
    int i = 0;
    for( ; number!= 0 ; ){
      i = i * 10;
      i = i + number%10;
      number = number/10;
   }
   return i;
}

int calc(int n){
    int reverse = rev(n);
    int ans;
    if(reverse < n && rev(reverse) == n){
        ans = min(v[n-1],v[reverse]) + 1;
    }else{
        ans = v[n-1] + 1;
    }
    //cout<<n<<" "<<reverse<<" "<<ans<<endl;
    return ans;
}

int main(){
	int T;
    
    REP(i,21){
        v.pb(i);
    }
    REPEAT(i,21,1000001){
        int n = calc(i);
        v.pb(n);
    }
	cin>>T;
	for(int x=1;x<=T;x++){
        int a;
        cin>>a;

        cout<<"Case #"<<x<<": ";
		cout<<v[a]<<endl;
		}
	return 0;
	}
	
