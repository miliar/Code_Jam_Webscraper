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
	int t,w;
	si(t);
	for(w=1;w<=t;w++){
		int n,m,i,j;
		si(n);
		int a[4][4];
		int b[4][4];
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				si(a[i][j]);
			}
		}
		si(m);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				si(b[i][j]);
			}
		}
		int flag=0;
		int r;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a[n-1][i]==b[m-1][j]){
					r=a[n-1][i];
					flag++;
				}	
			}
		}
		if(flag==0)
		printf("Case #%d: Volunteer cheated!\n",w);
		else if(flag==1)
		printf("Case #%d: %d\n",w,r);
		else
		printf("Case #%d: Bad magician!\n",w);
	}
	return 0;
}
