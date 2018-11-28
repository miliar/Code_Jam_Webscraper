/*************************************************************************
    > File Name: A.cpp
    > Author: milaso
    > Mail: 562058113@qq.com 
    > Created Time: 六  4/11 12:25:37 2015
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
char str[1010];
int main(){
	int T;
	scanf("%d",&T);
	for(int tt= 1 ;tt<=T;tt++){
		int maxk;
		memset(num,0,sizeof(num));
		scanf("%d",&maxk);
		scanf("%s",str);
		int ans=0,sum=0;
		for(int i=0;i<=maxk;i++){
			num[i] = str[i]-'0';
			if(sum < i) {
				ans ++;
			}
			sum = max(sum,i) + num[i];
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
