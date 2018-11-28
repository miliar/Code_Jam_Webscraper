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
	
	int sol[2][5] ; 
	int r ,a ; scanf("%d",&r);
	for(int i=0;i<4;i++){
		if( i == r-1 ){
			for(int j=0;j<4;j++)
				scanf("%d",&sol[0][j]);
		} else {
			for(int j=0;j<4;j++)
				scanf("%d",&a);
		}
	}
	scanf("%d",&r);
	for(int i=0;i<4;i++){
		if( i == r-1 ){
			for(int j=0;j<4;j++)
				scanf("%d",&sol[1][j]);
		} else {
			for(int j=0;j<4;j++)
				scanf("%d",&a);
		}
	}
	int c = 0 ; int ans ; 
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if( sol[0][i] == sol[1][j] ){
				ans = sol[0][i] ; 
				c++ ;
			}
		}
	}

	if( c == 1 )
		printf("Case #%d: %d\n",k,ans);
	else if( c == 0 )
		printf("Case #%d: Volunteer cheated!\n",k);
	else 
		printf("Case #%d: Bad magician!\n",k);
}

int main(int argc, char const *argv[]){
	
	freopen( "in.txt", "r",  stdin);
	freopen("out.txt", "w", stdout);
	
	int q ; scanf("%d",&q);
	
	for(int i=1;i<=q;i++) solve(i) ;
	
	return 0 ;

}

