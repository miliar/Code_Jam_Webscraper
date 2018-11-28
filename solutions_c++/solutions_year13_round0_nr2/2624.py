//Template

// By Anudeep :)
//Includes
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

//M lazy ;)
typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair< int ,int > pii;
typedef vector <ll> vll;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

int test=0;
int a[128][128],in[128][128];
void testcase() {
	test++;
	printf("Case #%d: ",test);
	int n,m,i,j,k;
	scanf("%d%d",&n,&m);
	rep(i,n) rep(j,m) scanf("%d",&in[i][j]);
	//Row wise
	rep(i,n) {
		int ma=-1;
		rep(j,m) ma = max(ma,in[i][j]);
		rep(j,m) a[i][j] = ma;
	}
	//col wise
	// rep(i,n) { rep(j,m) printf("%d ",a[i][j]); printf("\n"); }
	rep(j,m) {
		int ma=101;
		int flag = 1;
		rep(i,n) if(in[i][j] != a[i][j]) flag=0;
		if(flag) continue;
		rep(i,n) ma = min(ma,in[i][j]);
		// printf("%d %d\n",j,ma);
		rep(i,n) a[i][j] = ma;
	}
	int flag = 1;
	rep(i,n) rep(j,m) if(a[i][j]!=in[i][j]) flag=0;
	if(flag) printf("YES\n");
	else printf("NO\n");
}
	
int main() {
	int t;
	scanf("%d",&t);
	while(t--) testcase();
	return 0;
}