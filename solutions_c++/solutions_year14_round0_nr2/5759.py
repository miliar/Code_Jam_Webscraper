/* ***********************************************
Author :rabbit
Created Time :2014/4/13 0:58:11
File Name :G.cpp
************************************************ */
#pragma comment(linker, "/STACK:102400000,102400000")
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <string>
#include <time.h>
#include <math.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define pi acos(-1.0)
typedef long long ll;
int main()
{
     //freopen("B-small-attempt0.in","r",stdin);
    // freopen("B-small-attempt0.out","w",stdout);
     double C,F,X;
	 int T;
	 scanf("%d",&T);
	 for(int t=1;t<=T;t++){
		 scanf("%lf%lf%lf",&C,&F,&X);
		 printf("Case #%d: ",t);
         double ans=1e15;
         double r=2,tim=0;
         while(1){ 
      		double res=tim+X/r;
      		if(res<ans+eps)ans=res;
      		else break;
      		tim+=C/r;
      		r+=F;
     	 }
		 printf("%.7lf\n",ans);
	 }
     return 0;
}
