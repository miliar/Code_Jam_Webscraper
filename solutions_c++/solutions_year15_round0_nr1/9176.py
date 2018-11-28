#include <bits/stdc++.h>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define sc  scanf

#define sci(x) scanf("%d",&x)
#define scii(x,y) scanf("%d %d",&x,&y)
#define sciii(x,y,z) scanf("%d %d %d",&x,&y,&z)

#define scl(x) scanf("%lld",&x)
#define scll(x,y) scanf("%lld %lld",&x,&y)
#define sclll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)

#define scul(x) scanf("%llu",&x)

#define scf(x) scanf("%f",&x)
#define scff(x,y) scanf("%f %f",&x,&y)
#define scfff(x,y,z) scanf("%f %f %f",&x,&y,&z)

#define scd(x) scanf("%lf",&x)
#define scdd(x,y) scanf("%lf %lf",&x,&y)
#define scddd(x,y,z) scanf("%lf %lf %lf",&x,&y,&z)

#define pf printf
#define nnn pf("\n")
#define clr clear()
#define srt sort
#define pb push_back
#define ps push
#define sz size()
#define szo sizeof
#define frnt front
#define beg begin()
#define end end()
#define sqr(x) (x)*(x)
#define gc getchar()
#define PI 2*acos(0.0)
#define smlvlad 1e-11
#define smlvl 1e-10
#define mx 100001
#define mxAidx 16777680
#define Aidx (LL) e5+10
typedef unsigned long long ULL;
typedef long long LL;
typedef double DBL;
int main(){

	freopen("inf2.txt","r",stdin);
	freopen("of.txt","w",stdout);
	int Test,N,A[1010];
	char Z;
	sci(Test);
	for(int I=1;I<=Test;I++){
		sci(N); gc;
		for(int J=0;J<=N;J++){
			sc("%c",&Z);
			A[J]=Z-'0';
		}
		pf("Case #%d: ",I);
		int G=0,S=0;
		for(int J=0;J<=N;J++){
			if(S<J) {G+=J-S;S+=J-S;}
			S+=A[J];
		}
		pf("%d\n",G);
	}
	return 0;
}











