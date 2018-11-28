/* ***********************************************
Author :_rabbit
Created Time :2014/5/4 0:29:21
File Name :6.cpp
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
    // freopen("B-small-attempt0.in","r",stdin);
     //freopen("data.out","w",stdout);
     int a,b,k;
	 int T;
	 cin>>T;
	 for(int t=1;t<=T;t++){
		 cin>>a>>b>>k;
		 int ans=0;
		 for(int i=0;i<a;i++)
			 for(int j=0;j<b;j++)
				 if((i&j)<k)ans++;
		 printf("Case #%d: %d\n",t,ans);
	 }
     return 0;
}
