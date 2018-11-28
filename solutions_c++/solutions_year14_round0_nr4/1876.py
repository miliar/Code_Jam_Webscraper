#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define LL long long
#define mod 1000000007
#define maxn 1005
double a[maxn],b[maxn];
int main(){
	//freopen("in.in","r",stdin);
	//freopen("out","w",stdout);
	int t,cas = 0,n,sa,sb;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		sa = 0;sb = 0;
		for (int i = 0; i < n; i++)
			scanf("%lf",&a[i]);
		sort(a,a+n);
		for (int i = 0; i < n; i++)
			scanf("%lf",&b[i]);
		sort(b,b+n);
		int l1 = 0,l2 = 0;
		while(l1 < n && l2 < n){
			if(a[l1] > b[l2]){
				sa++;
				l1 ++ ;l2 ++;
			}else {
				l1++;
			}
		}
		l1 = 0,l2 = 0;
		while(l1 < n && l2 < n){
			if(a[l1] < b[l2]){
				sb++;
				l1 ++ ;l2 ++;
			}else {
				l2++;
			}
		}
		printf("Case #%d: %d %d\n",++cas,sa,n-sb);
	}
	return 0;
}