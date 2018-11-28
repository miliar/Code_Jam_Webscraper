#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long int llu;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI acos(-1)
#define S(a) scanf("%d",&a)
#define SL(a) scanf("%lld",&a)
#define S2(a, b) scanf("%d%d",&a,&b)
#define nl printf("\n")
#define DEB(x) cout<<#x<<" : "<<x<<endl;
const ll mod = 1000000007LL;
const int lmt = 100005;

int main(){
	freopen("inp.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	S(t);
	for(int tst = 1; tst <= t; tst++){
		int k, c, s;
		S2(k, c);
		S(s);
		printf("Case #%d: ",tst);
		for(int i = 1; i <= k; i++)
			printf("%d ",i);
		nl;
	}
	return 0;
}