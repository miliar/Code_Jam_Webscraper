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
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)
#define M 1000002013
int x[1024],y[1024],c[1024];
int arr[1024*2];
int testno=0;
ll cc[2500];
int solve() {
	memset(cc,0,sizeof(cc));
	int n,m,ptr=0;
	scanf("%d%d",&n,&m);
	ll prevans=0;
	rep(i,m) {
		scanf("%d%d%d",x+i,y+i,c+i);
		arr[ptr++] = x[i];
		arr[ptr++] = y[i];
		int ii = y[i]-x[i];
		prevans += (((((ll)ii*(ii-1))/2)%M)*c[i])%M;
		prevans %= M;
	}
	sort(arr,arr+ptr);
	// rep(i,ptr) printf("%d ",arr[i]); printf("\n");
	vi temp(arr,arr+ptr);
	unique(all(temp));
	rep(i,ptr) arr[i] = temp[i];
	// rep(i,ptr) printf("%d ",arr[i]); printf("\n");
	rep(i,ptr) if(i && arr[i]<=arr[i-1]) { ptr=i; break; }
	// rep(i,ptr) printf("%d ",arr[i]); printf("\n");
	rep(i,ptr-1) {
		cc[i]=0;
		rep(j,m) if(arr[i]>=x[j] && arr[i+1]<=y[j]) cc[i] += c[j];
	}
	ll ans = 0;
	ptr--;
	rep(i,ptr) {
		while(cc[i]!=0) {
			int start = cc[i];
			ll cmin = cc[i];
			int j;
			for(j=i+1;j<ptr && cc[j]!=0; j++) {
				cmin = min(cmin,cc[j]);
			}
			int ii = arr[j]-arr[i];
			//printf("%d %d\n",i,ii);
			ans += (((((ll)ii*(ii-1))/2)%M)*cmin)%M;
			ans %= M;
			for(j=j-1;j!=i-1;j--) cc[j] -= cmin;
		}
	}
	// printf("%lld %lld\n",ans,prevans);
	printf("Case #%d: %lld\n",++testno,(((ans-prevans)%M)+M)%M);
	return 0;
}

int main() {
	int t;
	scanf("%d",&t);
	while(t--) solve();
}