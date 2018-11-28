// LANG : C++

#include "cstdio"
#include "cstdlib"
#include "cstring"
#include "iostream"

#include "set"
#include "map"
#include "list"
#include "deque"
#include "queue"
#include "stack"
#include "string"
#include "vector"
#include "utility"
#include "algorithm"

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define S(x) (int)x.size()
#define Z(x) memset(x,0,sizeof(x))
#define D(a) cout << "[ " << #a << " : " << a << " ]"<< endl;

using namespace std;

typedef long long _lli;
typedef pair<int, int> _pii;
typedef vector<int> _vi;

void solve(int k){
	
	double cost , spdup , e ; scanf("%lf%lf%lf",&cost,&spdup,&e);
	
	double spd = 2.0 ; 
	
	double ans = 0 ; 
	
	while( (e/spd) > (cost/spd) + (e/(spd+spdup)) ){
		ans += cost/spd ; 
		spd+=spdup ;
	}
	ans += (e/spd);
	printf("Case #%d: %.7lf\n",k,ans);
	
}

int main(int argc, char const *argv[]){
	
	freopen( "3.txt", "r",  stdin);
	freopen("out.txt", "w", stdout);
	
	int q ; scanf("%d",&q);
	
	for(int i=1;i<=q;i++) solve(i) ;
	
	return 0 ;

}

