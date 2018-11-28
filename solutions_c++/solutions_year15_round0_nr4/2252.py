/*************************************************************************
    > File Name: B.cpp
    > Author: milaso
    > Mail: 562058113@qq.com 
    > Created Time: 六  4/11 13:24:43 2015
 ************************************************************************/

#include<iostream>
#include<math.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		int flag =1;
		if(r*c%x != 0) flag = 0;
		if((x+1)/2 > min(r,c)) flag = 0;
		if(x>6) flag= 0;
		if(x>3 && r*c/x == 2) flag = 0;
		if(x > max(r,c)) flag= 0;
		if(flag) printf("Case #%d: GABRIEL\n",tt);
		else     printf("Case #%d: RICHARD\n",tt);
	}
	return 0;
}
