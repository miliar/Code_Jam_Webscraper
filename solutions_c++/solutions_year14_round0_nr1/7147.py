// test.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<conio.h>
#include<map>
#include<queue>
#include <cstdio>
#include<iomanip>
#include<stack>
#include"windows.h"
#include <stdio.h>
#include<fstream>
#include <io.h>
using namespace std;

int T,r1,r2,x;
bool b1[20],b2[20];
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		memset(b1,0,sizeof b1);
		memset(b2,0,sizeof b2);
		scanf("%d",&r1);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&x);
				if(i==r1)b1[x]=1;
			}
		}
		scanf("%d",&r2);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&x);
				if(i==r2)b2[x]=1;
			}
		}
		int ans=-1,cnt=0;
		for(int i=1;i<=16;i++){
			if(b1[i]&&b2[i]){
				ans=i;
				cnt++;
			}
		}
		printf("Case #%d: ",cas);
		if(cnt==0)puts("Volunteer cheated!");
		else if(cnt>1)puts("Bad magician!");
		else printf("%d\n",ans);
	}
	return 0;
}