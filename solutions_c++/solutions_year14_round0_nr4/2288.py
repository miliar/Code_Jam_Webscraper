/* Nakshatra Maheshwari...!!!
  IIIT Allahabad....!! */

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<algorithm>
#define ll long long
#define mx7 10000007
#define mx6 1000006

//...........................................//
//input
#define si(t) scanf("%d",&t)
#define sl(t) scanf("%lld",&t)
#define sf(t) scanf("%f",&t)
#define sdb(t) scanf("%lf",&t)
#define schar(c) scanf("%c",&c)
#define sstr(s) scanf("%s",s)
#define ssi(a,b) scanf("%d%d",&a,&b)
#define ssl(a,b) scanf("%lld%lld",&a,&b)
//...........................................//
//Output
#define pi(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a)
#define pf(a) printf("%f\n",a)
#define pdb(a) printf("%lf\n",a)
//...........................................//
using namespace std;
int main(){
	int t,w=0;
	double a[1005],b[1005];
//	freopen("D-large.in","r",stdin);
//	freopen("out.txt","w",stdout);
	si(t);
	while(t--){
		int n,i,j;
		si(n);
		for(i=0;i<n;i++) 
		sdb(a[i]);
		for(i=0;i<n;i++) 
		sdb(b[i]);
		sort(a,a+n);
		sort(b,b+n);
		i=0;
		int ans1=0,ans2=0;
		for(j=0;j<n && i<n;){
			if(a[i]>b[j]){
				ans1++;
			//	printf("%lf %lf\n",a[i],b[j]);
				j++;
				i++;
			} else
			i++;
		}
		i=n-1;
		for(j=n-1;j>=0 && i>=0;i--){
			if(a[i]>b[j]){
				ans2++;
			} else
			j--;
		}
		printf("Case #%d: %d %d\n",++w,ans1,ans2);
	}
	return 0;
}
