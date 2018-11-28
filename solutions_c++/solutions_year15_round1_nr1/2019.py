/*************************************************************************
    > File Name: A.cpp
    > Author: milaso
    > Mail: 562058113@qq.com 
    > Created Time: 六  4/18 08:54:24 2015
 ************************************************************************/

#include<iostream>
#include<math.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;


int num[1010];

int main(){
	int T;
	scanf("%d",&T);
	for(int tt = 1;tt<=T;tt++){
		int n;
		scanf("%d",&n);
		int ans1= 0,ans2=0;
		int spd_10=0;
		scanf("%d",&num[0]);
		for(int i=1;i<n;i++){
			scanf("%d",&num[i]);
			if(num[i] < num[i-1]) {
				ans1 += num[i-1]-num[i];
				spd_10 = max(spd_10,num[i-1]-num[i]);
			}
		}
		for(int i=1;i<n;i++){
			ans2 += min(spd_10,num[i-1]);
		}
		printf("Case #%d: %d %d\n",tt,ans1,ans2);
	}
	return 0;
}
