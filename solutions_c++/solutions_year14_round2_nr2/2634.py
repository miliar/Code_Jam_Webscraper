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
int main()
{
//	freopen("11.in","r",stdin);
//	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int c1=1;c1<=t;c1++){
	int a,b,k,ret=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				ret++;
	printf("Case #%d: %d\n",c1,ret);
	}
	return 0;
}
