/*
* Filename:    D.cpp
* Desciption:  D
* Created:     2016年04月09日 21时19分57秒 星期六
* Author:      JIngwei Xu [mail:xu_jingwei@outlook.com]
*
*/
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;

//Init Const
const int INF=1e9;

//Global Variables
int K,C,S,t,ans;
//Function Declaration


//Main Program
int main()
{
#ifdef AC_THIS_PROBLEM
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
	//Init
	
	
	
	//Input
	scanf("%d",&t);
	for (int tcase = 1; tcase <=t; tcase += 1)
	{
		scanf("%d%d%d",&K,&C,&S);
		printf("Case #%d:",tcase);
		for(int i=1;i<=S;i++)printf(" %d",i);
		printf("\n");
		
	}
	return 0;
}

