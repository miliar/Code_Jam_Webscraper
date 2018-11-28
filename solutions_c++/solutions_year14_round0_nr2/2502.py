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
			double c,f,x;
			sdb(c);
			sdb(f);
			sdb(x);
			double ini=2.0;
			double sum=0.0;
			while(1){
				if(x/ini <= (c/ini + x/(ini+f))){
					sum+=x/ini;
					break;
				}
				sum+=c/ini;
				ini+=f;
			}
			printf("Case #%d: %.7lf\n",w,sum);
		}
		return 0;
	}
