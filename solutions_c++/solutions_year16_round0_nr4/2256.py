/* ***********************************************
Author        :axp
Created Time  :2016/4/9 14:55:31
TASK		  :smal.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int T;
int k,c,s;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",kase);
		for(int i=1;i<=k;i++)printf(" %d",i);
		putchar(10);
	}
    return 0;
}
