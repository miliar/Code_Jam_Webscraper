/* ***********************************************
Author :rabbit
Created Time :2014/4/13 0:17:56
File Name :4.cpp
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
int a[100][100],b[100][100];
int main()
{
     //freopen("A-small-attempt0.in","r",stdin);
     //freopen("A-small-attempt0.out","w",stdout);
     int T;
	 scanf("%d",&T);
	 for(int t=1;t<=T;t++){
		 int l,r;
		 scanf("%d",&l);
		 for(int i=1;i<=4;i++)
			 for(int j=1;j<=4;j++)scanf("%d",&a[i][j]);
		 scanf("%d",&r);
		 for(int i=1;i<=4;i++)
			 for(int j=1;j<=4;j++)
				 scanf("%d",&b[i][j]);
		 printf("Case #%d: ",t);
		 map<int,int> mp;
		 int id;
		 for(int i=1;i<=4;i++)mp[a[l][i]]=1;
		 int cnt=0;
		 for(int i=1;i<=4;i++)if(mp.find(b[r][i])!=mp.end())cnt++,id=b[r][i];
		 //cout<<"cnt="<<cnt<<endl;
		 if(cnt==0)puts("Volunteer cheated!");
		 else if(cnt==1)printf("%d\n",id);
		 else puts("Bad magician!");
	 }
     return 0;
}
