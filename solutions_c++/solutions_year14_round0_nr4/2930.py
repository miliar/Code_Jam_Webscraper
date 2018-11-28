#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
//#define maxn 50001
#define maxq 50001
#define maxe 100001
#define inf 100000007
#define ll long long
template <class T> T f_max(T x,T y){return x>y?x:y;}
template <class T> T f_min(T x,T y){return x<y?x:y;}
template <class T> void f_swap(T &x,T &y){T t;t=x,x=y,y=t;}
#define maxn 1001
double a[maxn];
double b[maxn];
int main(){
	int n;
	int t;

	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&t);
	int r,c,m;
	int i,j,cas;
	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf",&a[i]);
		for(i=0;i<n;i++) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int ans1=0,ans2=0;
		i=0,j=0;
		for(i=0;i<n;i++){
			if(j<n && a[i]>b[j]) ans1++,j++;
		}
		i=0,j=0;
		for(i=0;i<n;i++){
			if(j<n && b[i]>a[j]) ans2++,j++;
		}
		printf("Case #%d: %d %d\n",cas,ans1,n-ans2);
		
	}
	return 0;
}

/*


cccc.
ccc..
....*
*****
*/