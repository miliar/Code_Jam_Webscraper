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

int T,n;
double C,F,X;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%lf%lf%lf",&C,&F,&X);
		n=(X*F-(2.0)*C)/(C*F);
		double ans;
		if(n<0)ans=X/2.0;
		else{
		double dn=double(n);
		ans=X/(2.0+dn*F);
		for(int i=0;i<n;i++){
			double di=double(i);
			ans+=C/(2.0+di*F);
		}
		}
		printf("Case #%d: %.7f\n",cas,ans);
	}
	return 0;
}