#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
const int a[5][6]={1,1,4,1,1,10,2,2,2,6,2,2,1,1,7,1,1,19,1,1,7,9,1,19,2,2,14,10,2,92};
int i,j,k,n,m,an,te,T;
int main() {
	freopen("drum.in","r",stdin);
	freopen("drum.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d%d",&n,&m);
		an=0;
		For(i,1,m) {
			int d=__gcd(m,i);
			an+=a[n-2][d-1];
		}
		printf("Case #%d: %d\n",te,an/m);
		cerr<<an%m<<endl;
	}
	return 0;
}
