
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
typedef long long ll;
#define clr(x,a) memset(x,a,sizeof(x))
#define sz(x) (int)x.size()
#define see(x) cerr<<#x<<" "<<x<<endl
#define se(x) cerr<<" "<<x 
#define pb push_back
#define mp make_pair
#define rep(i,l,r) for (long long i=l;i<=r;i++)
using namespace std;
struct point{
	double r,c;
}a[1000];
int cmp(point a,point b){
	return a.c<b.c;
}
int n;
double V,X,d1,d2,ans;
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;cin>>T;
	for (int cas=1;cas<=T;cas++){
		scanf("%d%lf%lf",&n,&V,&X);
		for (int i=1;i<=n;i++){
			scanf("%lf%lf",&a[i].r,&a[i].c);
		}
		sort(a+1,a+1+n,cmp);
		for (int i=1;i<=n;i++){
		//	cout<<i<<" "<<a[i].r<<" "<<a[i].c<<endl;
		}
		if (n==1){
			if (X!=a[1].c) {
				printf("Case #%d: IMPOSSIBLE\n",cas);
			}
			else 
			printf("Case #%d: %.7lf\n",cas,V/a[1].r);
		}
		if (n==2){
			if (a[1].c==X && a[2].c==X){
				printf("Case #%d: %.7lf\n",cas,V/(a[1].r+a[2].r));
			}
			if (a[2].c==X && a[1].c!=X){
				printf("Case #%d: %.7lf\n",cas,V/a[2].r);
			}
			if (a[1].c==X && a[2].c!=X){
				printf("Case #%d: %.7lf\n",cas,V/a[1].r);
			}
			if (a[1].c>X || a[2].c<X){
				printf("Case #%d: IMPOSSIBLE\n",cas);
			}
			if (a[1].c<X && a[2].c>X){
				d1=X-a[1].c;
				d2=a[2].c-X;
				ans=max(V*(d2/(d1+d2))/a[1].r,V*(d1/(d1+d2))/a[2].r );
				printf("Case #%d: %.7lf\n",cas,ans);
			}
		}
	}
	return 0;
}

